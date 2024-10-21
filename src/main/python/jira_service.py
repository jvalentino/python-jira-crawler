from url_util import UrlUtil
import requests
from urllib.parse import quote
from epic import Epic
import os
import json
import concurrent.futures
from story import Story

class JiraService:
    def __init__(self):
        # Initialize any necessary variables or state here
        pass
    
    def validate(self, settings, auth):
        print("  jira_service.py: validate()")
        
        url = settings.base_url + '/rest/api/3/myself'
        print(f"   URL: {url}")
        print(f"   AUTH: {auth}")
        
        try:
            response = UrlUtil.http_get(url, auth)
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
            raise
        

    def pull_epics(self, settings, auth):
        print("  jira_service.py: pull_epics()")
        
        # Check if target/epics.json exists
        file_path = 'target/epics.json'
        if os.path.exists(file_path):
            print(f"   Loading epics from {file_path}")
            with open(file_path, 'r') as file:
                epics = json.load(file)
                return [Epic(**epic) for epic in epics]
        
        encoded_jql = quote(settings.epic_jql)
        url = f"{settings.base_url}/rest/api/3/search?jql={encoded_jql}"
        
        raw_epics = UrlUtil.http_get_pagination(url, auth)
        print(f"   Found {len(raw_epics)} epics")
        
        # now parse all the epics
        epics = []
        for raw_epic in raw_epics:
            epic = Epic()
            
            epic.title = raw_epic.get('fields', {}).get('summary', '')
            epic.due_date = raw_epic.get('fields', {}).get(settings.epic_due_date_field, '')
            epic.key = raw_epic.get('key', '')
            epic.start_date = raw_epic.get('fields', {}).get(settings.epic_start_date_field, '')
            
            # Safely get the assignee's display name
            assignee = raw_epic.get('fields', {}).get('assignee')
            if assignee:
                epic.assignee_name = assignee.get('displayName', '')
                epic.assignee_email = assignee.get('emailAddress', '')
                epic.assignee_icon = assignee.get('avatarUrls', {}).get('48x48', '')            
            
            
            # attempt to look up their groupings from the settings
            for grouping_name, epic_keys in settings.groupings.items():
                    if epic.key in epic_keys:
                        epic.grouping = grouping_name
                        # print(f"   Found grouping {grouping_name} for epic {epic.key}")
                        break
            
            # Only keep epics that have start and end dates
            if (epic.start_date == None or epic.start_date == '') or (epic.due_date == None or epic.due_date == ''):
                print(f"   X {epic}")
                continue    
            
            print(f"   + {epic}")
            epics.append(epic)
        
        # Write the result to target/epics.json
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump([epic.to_dict() for epic in epics], file, indent=4)
        
        return epics
        
    def pull_stories(self, settings, auth, epics):
        print(f"  jira_service.py: pull_stories()")
        
        # Check if target/epics.json exists
        file_path = 'target/epic_with_stories.json'
        if os.path.exists(file_path):
            print(f"   Loading epics from {file_path}")
            with open(file_path, 'r') as file:
                epics = json.load(file)
                return [Epic(**epic) for epic in epics]

        def fetch_stories_for_epic(epic):
            jql = f'"Epic Link" = {epic.key}'
            encoded_jql = quote(jql)
            url = f"{settings.base_url}/rest/api/3/search?jql={encoded_jql}"
            stories = UrlUtil.http_get_pagination(url, auth)
            return stories


        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_epic = {executor.submit(fetch_stories_for_epic, epic): epic for epic in epics}
            for future in concurrent.futures.as_completed(future_to_epic):
                epic = future_to_epic[future]
                try:
                    stories = future.result()
                    # pase the stories and add them to the epic
                    parsed_stories = [self.parse_story(settings, raw_story) for raw_story in stories]
                    print(f"   Fetched {len(stories)} stories for epic {epic.key}")
                    epic.stories = parsed_stories
                except Exception as exc:
                    print(f"   Epic {epic.key} generated an exception: {exc}")
                    
        # write the result to target/epic_with_stories.json
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump([epic.to_dict() for epic in epics], file, indent=4)


    def parse_story(self, settings, raw_story):
        story = Story()
        story.title = raw_story.get('fields', {}).get('summary', '')
        story.key = raw_story.get('key', '')
        story.status = raw_story.get('fields', {}).get('status', {}).get('name', '')
        story.points = raw_story.get('fields', {}).get(settings.story_point_field, 0.0)
        return story
        