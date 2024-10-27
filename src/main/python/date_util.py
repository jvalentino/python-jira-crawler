from datetime import datetime, timedelta

def yyyy_mm_dd_to_date(yyyy_mm_dd):
    return datetime.strptime(yyyy_mm_dd, '%Y-%m-%d').date()

def date_to_yyyy_mm_dd(date):
    return date.strftime('%Y-%m-%d')

def current_yyyy_mm_dd_as_string():
    return datetime.now().strftime('%Y-%m-%d')

def find_first_index_after_date(date_list, current_date_str):
    # Convert the current date string to a datetime object
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    
    # Iterate through the list of dates
    for index, date_str in enumerate(date_list):
        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Check if the date is equal to or after the current date
        if date >= current_date:
            return index
    
    # If no date is found, return -1
    return -1