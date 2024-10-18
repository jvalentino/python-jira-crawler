from url_util import UrlUtil
import requests
from urllib.parse import quote
from epic import Epic
import os
import json

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
            
            # TODO: Only keep epics that have start and end dates
            
            print(f"   {epic}")
            epics.append(epic)
        
        # Write the result to target/epics.json
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump([epic.__dict__ for epic in epics], file, indent=4)
        
        return epics
        
        