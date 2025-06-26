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

def list_tasks(today_only=False):
    tasks = load_tasks()
    if today_only:
        tasks = filter_today_tasks(tasks)
        print("📅 Tasks Due Today:")
   
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task.id != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"❌ Task with ID {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"🗑️ Task {task_id} deleted.")
        
        
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.mark_complete()
            save_tasks(tasks)
            print(f"✅ Task {task_id} marked as complete.")
            return
        
        
def main():
    parser = argparse.ArgumentParser(description="📝 CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--due", help="Due date (YYYY-MM-DD)", required=False)

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--today", action="store_true", help="Only show tasks due today")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID to mark complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description, args.due)
    elif args.command == "list":
        list_tasks(today_only=args.today)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
        main()
