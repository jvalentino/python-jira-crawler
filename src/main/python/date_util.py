from datetime import datetime, timedelta

def yyyy_mm_dd_to_date(yyyy_mm_dd):
    return datetime.strptime(yyyy_mm_dd, '%Y-%m-%d').date()

def date_to_yyyy_mm_dd(date):
    return date.strftime('%Y-%m-%d')