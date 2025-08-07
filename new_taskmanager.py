import json
import os

TASKS_FILE="task.json"

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
        status = "*" if task["completed"] else "x"
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

def delete_hhtask(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted.")


def show_help():
    print("""
Usage:
    python task_manager.py add "Task Title"
    python task_manager.py view
    python task_manager.py complete <task_id>
    python task_manager.py delete <task_id>
""")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) >= 3:
                title = " ".join(sys.argv[2:])
                add_task(title)
            else:
                print("Please provide a task title.")
        elif command == "view":
            view_tasks()
        elif command == "complete":
            if len(sys.argv) == 3 and sys.argv[2].isdigit():
                complete_task(int(sys.argv[2]))
            else:
                print("Please provide a valid task ID.")
        elif command == "delete":
            if len(sys.argv) == 3 and sys.argv[2].isdigit():
                delete_task(int(sys.argv[2]))
            else:
                print("Please provide a valid task ID.")
        else:
            show_help()
            