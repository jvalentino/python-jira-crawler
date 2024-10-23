from epic_grouping import EpicGrouping
from epic_setting import EpicSetting
from chart_settings import ChartSettings
import json

class ChartingService:
    def __init__(self):
        pass
    
    def chart_settings_to_json(self, file_path, chart_settings):
        with open(file_path, 'w') as file:
            json.dump(chart_settings, file, indent=4, default=lambda o: o.__dict__)

    def generate_groupings(self, epics):
        print("  charting_service.py: generate_groupings()")
        groupings = []
        current_grouping = None
        previous_grouping_name = None
        
        # for each epic
        for epic in epics:
            
            # if the current grouping is different, this is a new grouping
            if epic.grouping != previous_grouping_name:
                current_grouping = EpicGrouping(grouping=epic.grouping)
                current_grouping.epic_settings = []
                groupings.append(current_grouping)
            
            # Create a new Epic Setting
            epic_setting = EpicSetting(epic=epic)
            current_grouping.epic_settings.append(epic_setting)
            #print(f"    {epic.grouping} adding {epic.title}")
            
            previous_grouping_name = epic.grouping
            
        
        # for each grouping
        for grouping in groupings:
            print(f"   {grouping.grouping} has {len(grouping.epic_settings)} epics")
        
        chart_settings = ChartSettings(epic_groupings=groupings)
        
        self.chart_settings_to_json('target/chart_settings_initial.json', chart_settings)
        return chart_settings