# execution_handler.py
from jira_service import JiraService
from settings import load_settings_from_yaml

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
        
        print(" (2) Obtain Jira Epics")
        epics = self.jira_service.pull_epics()
        
        print(" (3) Obtain Jira Stories")
        
        print(" (4) Figure out how to organize in a Gantt")
        
        print(" (5) Generate Gantt")
        
        

