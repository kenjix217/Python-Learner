"""
Models for the Task Manager Application.
"""
from datetime import datetime

class Task:
    """Represents a single task."""
    
    def __init__(self, title, description, due_date=None, completed=False, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.created_at = datetime.now().isoformat()

    def mark_complete(self):
        """Mark task as complete."""
        self.completed = True

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.title} (ID: {self.id})"
