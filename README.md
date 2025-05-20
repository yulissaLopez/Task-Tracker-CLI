# 📝 Task Tracker CLI

A simple command-line interface (CLI) tool to manage your tasks efficiently using Python and JSON.

---

## 📦 Features

- Add new tasks with a description.
- List all tasks or filter by status (pending/completed).
- Mark tasks as completed or delete them.
- Edit task details.
- Persistent storage using a JSON file.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6+ installed:

## Usage
python task_app.py [command] [options]

### Available Commands
# Add a task
python task_app.py add "Buy groceries"
# Add a task with description
python task_app.py add "Buy groceries" --desc  "tomatos and carrots"

# Update and delete task
task_app.py update fcd66b47-8dd0-4e7d-bc0d-bf6c187b40ec --title "Buy groceries and cook dinner"
task_app.py update fcd66b47-8dd0-4e7d-bc0d-bf6c187b40ec --title "Buy groceries and cook dinner" --desc ""
task_app.py delete 01290252-5431-430b-b9fb-d834ec52046f

# Marking a task as in progress, done, pending
python task_app.py set-status [task id] [status option]
python task_app.py set-status 2da2d176-c1ef-4a86-9ce9-3e9f7022f13b done

# List all tasks
python task_app.py list

# Listing tasks by status
task_app.py list-done
task_app.py list-pending
task_app.py list-progress



