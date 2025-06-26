import json
import os
from task import Task
from datetime import date

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file and return a list of Task instances."""
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            return [Task(**task) for task in data]
    except (json.JSONDecodeError, IOError):
        print("❌ Error reading tasks.json. Returning empty list.")
        return []

def save_tasks(tasks):
    """Save a list of Task instances to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def get_next_id(tasks):
    """Return the next task ID based on the highest current ID."""
    return max((task.id for task in tasks), default=0) + 1

def filter_today_tasks(tasks):
    """Return only tasks that are due today."""
    today = date.today().isoformat()
    return [task for task in tasks if task.due_date == today]
