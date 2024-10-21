# epic.py

class Epic:
    def __init__(self, key=None, due_date=None, start_date=None, title=None, 
                 assignee_name=None, assignee_email=None, assignee_icon=None):
        self.key = key
        self.due_date = due_date
        self.start_date = start_date
        self.title = title
        self.assignee_name = assignee_name
        self.assignee_email = assignee_email
        self.assignee_icon = assignee_icon
        

    def __repr__(self):
        return (f"Epic(key={self.key}, due_date={self.due_date}, "
                f"start_date={self.start_date}, title={self.title})")
