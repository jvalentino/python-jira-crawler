from epic_grouping import EpicGrouping
from epic_setting import EpicSetting
from chart_settings import ChartSettings
import json
from datetime import datetime, timedelta
from date_util import yyyy_mm_dd_to_date, date_to_yyyy_mm_dd

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
        print("   Initial settings written to target/chart_settings_initial.json")
        return chart_settings
    
    def update_with_positions(self, chart_settings):
        print("  charting_service.py: determine_row_and_column()")
        
        # figure out the time range
        chart_settings.date_min, chart_settings.date_max = self.get_min_max_dates(chart_settings)
        print(f"   Dates: {chart_settings.date_min} to {chart_settings.date_max}")     
        
        # figure out the weeks between the dates
        chart_settings.weeks = self.get_weeks_between_dates(chart_settings.date_min, chart_settings.date_max) 
        print(f"   Weeks: {chart_settings.weeks}")
        
        # the min row is always going to be 0
        chart_settings.row_min = 0
        print(f"   row min: {chart_settings.row_min}")
        
        # the min column is always going to be 0
        chart_settings.column_min = 0
        print(f"   column min: {chart_settings.column_min}")
        
        # the max column is always going to be the number of weeks - 1
        chart_settings.column_max = chart_settings.weeks - 1
        print(f"   column max: {chart_settings.column_max}")
        
        # now the hard part, which is figuring out the row and column group by group
        for grouping in chart_settings.epic_groupings:
            self.process_grouping(chart_settings, grouping)
        
        self.chart_settings_to_json('target/chart_settings_final.json', chart_settings)
        print("   Initial settings written to target/chart_settings_final.json")

                
    def get_min_max_dates(self, chart_settings):
        dates = []
        # for each grouping
        for grouping in chart_settings.epic_groupings:
            # for each epic setting
            for epic_setting in grouping.epic_settings:
                dates.append(epic_setting.epic.start_date)
                dates.append(epic_setting.epic.due_date)
                
        dates.sort()
        earliest_date = dates[0]
        latest_date = dates[-1]
        
        return earliest_date, latest_date
        
    def get_weeks_between_dates(self, date_str1, date_str2, date_format="%Y-%m-%d"):
        # Parse the date strings into datetime objects
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        
        # Calculate the difference between the two dates
        delta = date2 - date1
        
        # Convert the difference into weeks
        weeks = delta.days / 7
        return weeks
    
    def get_mapping_of_date_to_column(self, chart_settings):
        date_to_column = {}
        # use min date
        start_date = yyyy_mm_dd_to_date(chart_settings.date_min)
        for i in range(chart_settings.weeks + 1):
            date = start_date + timedelta(weeks=i)
            date_to_column[date_to_yyyy_mm_dd(date)] = i
            
        
        return date_to_column
    
    def process_grouping(self, chart_settings, grouping):
        # create a mapping of date to column
        date_to_column = {}
        
        # for each epic in this grouping
        for epic_setting in grouping.epic_settings:
            # the start end end column are always fixed, and based on start and due date
            pass