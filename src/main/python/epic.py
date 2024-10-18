# epic.py

class Epic:
    def __init__(self, key=None, due_date=None, start_date=None, title=None):
        self.key = key
        self.due_date = due_date
        self.start_date = start_date
        self.title = title

    def __repr__(self):
        return (f"Epic(key={self.key}, due_date={self.due_date}, "
                f"start_date={self.start_date}, title={self.title})")

# Example usage
if __name__ == "__main__":
    # Create an instance of the Epic class
    epic = Epic(key="EPIC-123", due_date="2023-12-31", start_date="2023-01-01", title="Example Epic")
    
    # Print the instance
    print(epic)