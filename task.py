from datetime import datetime

class Task:
    def __init__(self, id, title, description, due_date=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed


    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
      return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "due_date": self.due_date,
        "completed": self.completed
      }


    def __str__(self):
        """Return a readable string representation of the task."""
        status = "✅" if self.completed else "❌"
        due = self.due_date if self.due_date else "No due date"
        return f"[{status}] {self.id}: {self.title} — {self.description} (Due: {due})"
