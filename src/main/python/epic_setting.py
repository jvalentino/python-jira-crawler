class EpicSetting:
    def __init__(self, epic=None, row=-1, column_start=-1, column_end=-1):
        self.row = row
        self.column_start = column_start
        self.column_end = column_end
        self.alpha_key = None
        self.friendly_name = None
        self.friendly_assigned = None
        self.percent_complete = None
        self.percent_in_progress = None
        self.percent_not_started = None
        self.epic = epic
    