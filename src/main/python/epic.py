# epic.py
from story import Story

class Epic:
    def __init__(self, key=None, due_date=None, start_date=None, title=None, 
                 assignee_name=None, assignee_email=None, assignee_icon=None, 
                 story_points=0.0, story_count=0, story_points_completed=0.0, 
                 story_points_in_progress=0.0, story_points_todo=0.0, 
                 story_count_completed=0, story_count_in_progress=0, 
                 story_count_todo=0, stories=None):
        self.key = key
        self.due_date = due_date
        self.start_date = start_date
        self.title = title
        self.assignee_name = assignee_name
        self.assignee_email = assignee_email
        self.assignee_icon = assignee_icon
        self.story_points = story_points
        self.story_count = story_count
        self.story_points_completed = story_points_completed
        self.story_points_in_progress = story_points_in_progress
        self.story_points_todo = story_points_todo
        self.story_count_completed = story_count_completed
        self.story_count_in_progress = story_count_in_progress
        self.story_count_todo = story_count_todo
        self.stories = stories if stories is not None else []
        

    def __repr__(self):
        return (f"Epic(key={self.key}, due_date={self.due_date}, "
                f"start_date={self.start_date}, title={self.title})")
# Example usage
if __name__ == "__main__":
    # Create an instance of the Epic class with no parameters
    epic_default = Epic()
    print(epic_default)

    # Create an instance of the Epic class with parameters
    story1 = Story(key="STORY-123", title="Example Story 1", status="In Progress", points=5)
    story2 = Story(key="STORY-456", title="Example Story 2", status="Done", points=8)
    epic_with_params = Epic(
        key="EPIC-123", due_date="2023-12-31", start_date="2023-01-01", title="Example Epic",
        assignee_name="John Doe", assignee_email="john.doe@example.com", assignee_icon="icon_url",
        story_points=13.0, story_count=2, story_points_completed=8.0, 
        story_points_in_progress=5.0, story_points_todo=0.0, 
        story_count_completed=1, story_count_in_progress=1, 
        story_count_todo=0, stories=[story1, story2]
    )
    print(epic_with_params)