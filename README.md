# 📝 Python CLI To-Do App

This is a command-line to-do list manager written in Python. It helps you track your tasks from the terminal!

## 🚀 Features

- Add tasks with title, description, and optional due date
- List all tasks or just today's tasks
- Mark tasks as completed
- Delete tasks by ID
- Tasks are saved in `tasks.json` for persistence

## 📦 How to Run

<!--
```bash
python app.py add "Learn Git" "Push final project" --due 2025-06-19
python app.py list
python app.py list --today
python app.py complete 1
python app.py delete 1
``` -->

# Add a new task with an optional due date

python app.py add "Learn Git" "Push final project" --due 2025-06-19

# List all tasks

python app.py list

# List only tasks due today

python app.py list --today

# Mark a task as completed (replace 1 with the task ID)

python app.py complete 1

# Delete a task by ID

python app.py delete 1
