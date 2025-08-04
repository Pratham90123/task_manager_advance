
import json
import os

TASK_FILE="task.json"

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {title}")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f"{task['id']}. {task['title']} - {status}")