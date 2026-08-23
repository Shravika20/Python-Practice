def add_task():
    task = input("Enter your task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task.strip())
    except FileNotFoundError:
        print("No tasks found.")
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")