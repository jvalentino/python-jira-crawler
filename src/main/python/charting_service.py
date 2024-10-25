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
            
            # format the epic name
            epic_setting.friendly_name = self.extract_text_after_last_bracket(epic.title)
            epic_setting.friendly_assigned = self.abbreviate_name(epic.assignee_name)
            
            # figure out the % complete
            if (epic.story_points == 0):
                epic_setting.percent_complete = 0
                epic_setting.percent_in_progress = 0
                epic_setting.percent_not_started = 0
            else:
                epic_setting.percent_complete = epic.story_points_completed / epic.story_points
                epic_setting.percent_in_progress = epic.story_points_in_progress / epic.story_points
                epic_setting.percent_not_started = 1 - epic_setting.percent_complete - epic_setting.percent_in_progress
            
            previous_grouping_name = epic.grouping
            
        
        # for each grouping
        for grouping in groupings:
            print(f"   {grouping.grouping} has {len(grouping.epic_settings)} epics")
        
        chart_settings = ChartSettings(epic_groupings=groupings)
        
        self.chart_settings_to_json('target/chart_settings_initial.json', chart_settings)
        print("   Initial settings written to target/chart_settings_initial.json")
        return chart_settings
    
    def abbreviate_name(self, name):
        # Check if the input is None or empty
        if not name:
            return ""
        
        # Split the name into parts based on space or dot
        if '.' in name:
            parts = name.split('.')
        else:
            parts = name.split()
        
        # Capitalize the first letter of each part
        parts = [part.capitalize() for part in parts]
        
        # If there's only one part, return it as is
        if len(parts) == 1:
            return parts[0]
        
        # Get the first name and the initial of the last name
        first_name = parts[0]
        last_initial = parts[1][0] if len(parts) > 1 else ""
        
        # Return the formatted name
        return f"{first_name} {last_initial}"
    
    def extract_text_after_last_bracket(self, input_string):
        # Find the last occurrence of '[' or ']'
        last_bracket_index = max(input_string.rfind('['), input_string.rfind(']'))
        
        # If no bracket is found, return an empty string
        if last_bracket_index == -1:
            return ""
        
        # Extract the content after the last bracket and trim whitespace
        result = input_string[last_bracket_index + 1:].strip()
        
        return result
    
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
        
        # the max column is always going to be the number of weeks
        chart_settings.column_max = chart_settings.weeks 
        print(f"   column max: {chart_settings.column_max}")
        
        # create a mapping of date to column
        chart_settings.date_to_column = self.get_mapping_of_date_to_column(chart_settings)
        
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
        weeks = delta.days // 7
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
        
        # FiXME: Need to check first and see if start and end dates are in the mapping
        
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # for each epic in this grouping
        alphabet_index = 0
        for epic_setting in grouping.epic_settings:
            # the start end end column are always fixed, and based on start and due date
            epic_setting.column_start = chart_settings.date_to_column[epic_setting.epic.start_date]
            epic_setting.column_end = chart_settings.date_to_column[epic_setting.epic.due_date] -1
            
            # assign a single letter to represent this epic in this group
            epic_setting.alpha_key = alphabet[alphabet_index]
            alphabet_index += 1
            
        # for each epic, need to figure out the row
        for epic_setting in grouping.epic_settings:
            # determine the first row where nothing overlaps
            current_row = 0
            while (True):
                # if the current row is not already taken
                if not self.does_epic_overlap(current_row, epic_setting, grouping.epic_settings):
                    epic_setting.row = current_row
                    break
                
                current_row += 1
        
        # determine the row_max in this grouping
        grouping.row_max = max([epic_setting.row for epic_setting in grouping.epic_settings])
        grouping.column_max = max([epic_setting.column_end for epic_setting in grouping.epic_settings])
        grouping.column_min = min([epic_setting.column_start for epic_setting in grouping.epic_settings])
        
        # now print the grouping in ASCII style format
        self.print_grouping(chart_settings, grouping)
            
                
    def does_epic_overlap(self, current_row, given_epic_setting, epic_settings):
        # for each epic in the grouping
        for current_epic_setting in epic_settings:
            # if the current epic is the same as the given epic, skip
            if current_epic_setting.epic.key == given_epic_setting.epic.key:
                continue
            
            # if the current epic is not on the same row we are checking, skip it
            if current_epic_setting.row != current_row:
                continue
            
            # if there is any overlap between start and end columns
            if (current_epic_setting.column_start <= given_epic_setting.column_end and
                current_epic_setting.column_end >= given_epic_setting.column_start):
                return True
            
        # there is no overlap   
        return False
    
    def print_grouping(self, chart_settings, grouping):
        print("")
        print(f"{grouping.grouping}")
        # show the codes for each epic
        for epic_setting in grouping.epic_settings:
            print(f"- {epic_setting.alpha_key}{epic_setting.alpha_key}: [{epic_setting.epic.key}] {epic_setting.epic.title}")
        
        print("")
        
        # draw the columns
        print("   ", end="")
        for i in range(chart_settings.column_max + 1):
            print(f"{str(i).zfill(2)} ", end="")
        print("")
        
        # for each row...
        for i in range(grouping.row_max + 1):
            # print the row number
            print(f"{str(i).zfill(2)} ", end="")
            
            # print all epics on this row
            self.print_epics_on_row(i, chart_settings.column_max, grouping.epic_settings)
            
        
        print("")
        
    def print_epics_on_row(self, row, column_max, epic_settings):
        # Create a list to store the output for the row
        row_output = ["   "] * (column_max + 1)
        
        # for each epic in the grouping
        for epic_setting in epic_settings:
            # if the epic is on this row
            if epic_setting.row == row:
                # for each column in the epic's range
                for i in range(epic_setting.column_start, epic_setting.column_end + 1):
                    row_output[i] = f"{epic_setting.alpha_key}{epic_setting.alpha_key} "
        
        # Print the row output
        print("".join(row_output))