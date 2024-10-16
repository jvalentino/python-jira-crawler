from url_util import UrlUtil
import requests

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
            print(response)
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
            # Handle the exception or re-raise it
            raise
        

    def pull_epics(self):
        print("  jira_service.py: pull_epics()")