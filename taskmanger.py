
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {title}")

