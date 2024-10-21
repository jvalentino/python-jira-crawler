from epic_grouping import EpicGrouping
from epic_setting import EpicSetting

class ChartingService:
    def __init__(self):
        pass

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
            
        return groupings