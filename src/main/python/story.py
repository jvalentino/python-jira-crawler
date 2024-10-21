# story.py

class Story:
    def __init__(self, key=None, title=None, status=None, points=None):
        self.key = key
        self.title = title
        self.status = status
        self.points = points

    def __repr__(self):
        return (f"Story(key={self.key}, title={self.title}, "
                f"status={self.status}, points={self.points})")
