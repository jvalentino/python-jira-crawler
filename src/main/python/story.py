# story.py

class Story:
    def __init__(self, key=None, title=None, status=None, points=None):
        self.key = key
        self.title = title
        self.status = status
        self.points = points

    def to_dict(self):
        return {
            'key': self.key,
            'title': self.title,
            'status': self.status,
            'points': self.points
        }

    def __repr__(self):
        return (f"Story(key={self.key}, title={self.title}, "
                f"status={self.status}, points={self.points})")

# Example usage
if __name__ == "__main__":
    # Create an instance of the Story class with no parameters
    story_default = Story()
    print(story_default)

    # Create an instance of the Story class with parameters
    story_with_params = Story(key="STORY-123", title="Example Story", status="In Progress", points=5)
    print(story_with_params)