
class ChartSettings:
    def __init__(self, epic_groupings=[]):
       self.date_min = None
       self.date_max = None
       self.row_min = -1
       self.row_max = -1
       self.column_min = -1
       self.column_max = -1
       self.weeks = -1
       self.date_to_column = {}
       self.epic_groupings = epic_groupings
       