# todo.py

import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Read tasks from file; create file if not exists."""
    if not os.path.exists(TASK_FILE):
        open(TASK_FILE, "w").close()
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    """Write all tasks back to file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added task: \"{task}\"")
    else:
        print("Empty task not added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed task: \"{removed}\"")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid integer.")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== To‑Do List Menu ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice (1‑4): ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting. Bye!")
            break
        else:
            print("Invalid choice; please enter 1‑4.")

if __name__ == "__main__":
    main()
