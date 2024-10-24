# execution_handler.py
from jira_service import JiraService
from settings import load_settings_from_yaml
import os
import requests
from epic import Epic
from charting_service import ChartingService

class ExecutionHandler:
    jira_service = JiraService()
    charting_service = ChartingService()
    
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
        updated_epics = self.jira_service.pull_stories(settings, auth, epics)
        print(f"  {len(updated_epics)} epics")
        print("")
        
        print(" (4) Generating Epic Stats")
        self.jira_service.update_with_stats(settings, updated_epics)
        print("")
        
        print(" (5) Figure out how to organize in a Gantt")
        chart_settings = self.charting_service.generate_groupings(updated_epics)
        print("")
        
        print(" (6) Generate row and column positions")
        self.charting_service.update_with_positions(chart_settings)
        print("")
        
        print(" (7) Generate Gantt")
        
        

