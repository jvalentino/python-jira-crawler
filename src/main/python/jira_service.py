from url_util import UrlUtil
import requests
from urllib.parse import quote

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
        
        encoded_jql = quote(settings.epic_jql)
        url = f"{settings.base_url}/rest/api/3/search?jql={encoded_jql}"
        
        epics = UrlUtil.http_get_pagination(url, auth)
        print(f"   Found {len(epics)} epics")
        
        return epics
        
        