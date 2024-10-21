# execution_handler.py
from jira_service import JiraService
from settings import load_settings_from_yaml
import os
import requests
from epic import Epic

class ExecutionHandler:
    jira_service = JiraService()
    
    def __init__(self):
        # Initialize any necessary variables or state here
        pass

    def run(self):
        print("execution_handler.py: run()")
        
        print(" (1) Loading Settings")
        settings = load_settings_from_yaml('settings.yaml')
        print(f"  {settings}")
        print("")
        
        print(" (2) Obtain Jira Epics")
        auth = os.getenv(settings.auth_env_var, '')
        try:
            self.jira_service.validate(settings, auth)
        except requests.exceptions.RequestException as e:
            raise
        
        epics = self.jira_service.pull_epics(settings, auth)
        print(f"  {len(epics)} epics parsed")
        print("")
        
        print(" (3) Obtain Jira Stories")
        # self.jira_service.pull_stories(settings, auth, epics)
        
        print(" (4) Figure out how to organize in a Gantt")
        
        print(" (5) Generate Gantt")
        
        

