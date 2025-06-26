import argparse
from task import Task
from utils import load_tasks, save_tasks, get_next_id, filter_today_tasks

def add_task(title, description, due_date=None):
    tasks = load_tasks()
    task_id = get_next_id(tasks)
    new_task = Task(task_id, title, description, due_date)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task added with ID {task_id}.")

def main():
    parser = argparse.ArgumentParser(description="📝 CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")
    ...
    if __name__ == "__main__":
        main()
