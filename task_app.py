import json
import os
import uuid
import argparse

FILE = 'task.json'

# Funcion que cargue las tareas de mi archivo
def load_task():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)
    
# Funcion que guarde las tareas en json
def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# Funcion que anadir las tareas
def add_task(title, description =""):
    tasks = load_task()

    new_task = {
        "id" : str(uuid.uuid4()),
        "title" : title,
        "description" : description,
        "status" : "pending"
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea {new_task["id"]:^6} agregada ")

#Funcion que actualiza las tareas 
def update_task(task_id, title=None, description=None):
    tasks = load_task()

    for task in tasks:
        if task["id"] == task_id:
            if title: task["title"] = title
            if description: task["description"] = description
            save_tasks(tasks)
            print("Tarea actualizada")
            return
    print("Tarea no encontrada")

#Funcion que elimina las tareas
def delete_task(task_id):
    tasks = load_task()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print("Tarea eliminada")

#Funcion que cambia el estado de la tarea
def set_status(task_id, status):
    if status not in ["pending", "in_progress", "done"]:
        print("Estado Invalido")
        return
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print("Estado actualizado.")
            return
    print("Tarea no encontrada")

# Funcion para listar las tareas
def list_task(filter_status=None):
    tasks = load_task()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    for t in tasks:
        print(f"{t["status"]:^20} {t["id"]:^20}  {t['title']:^20}")
        #print("Estado: {0:^4} ID: {1:^4} Tarea: {2:^4}".format(t["status"], t["id"], t['title']))
def main():
    parser = argparse.ArgumentParser(description="Task Traker")

    subparsers = parser.add_subparsers(dest = "command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--desc", default="")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id")
    update_parser.add_argument("--title")
    update_parser.add_argument("--desc")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id")

    status_parser = subparsers.add_parser("set-status")
    status_parser.add_argument("id")
    status_parser.add_argument("status", choices=["pending", "in_progress", "done"])

    list_all = subparsers.add_parser("list")
    list_done = subparsers.add_parser("list-done")
    list_pending = subparsers.add_parser("list-pending")
    list_progress = subparsers.add_parser("list-progress")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.desc)
    elif args.command == "update":
        update_task(args.id, args.title, args.desc)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "set-status":
        set_status(args.id, args.status)
    elif args.command == "list":
        list_task()
    elif args.command == "list-done":
        list_task("done")
    elif args.command == "list-pending":
        list_task("pending")
    elif args.command == "list-progress":
        list_task("in_progress")

if __name__ == "__main__":
    main()


