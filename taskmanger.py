
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


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted.")