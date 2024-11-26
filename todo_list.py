todos = []

def add_todo():
    task = input("Enter a new task: ")
    todos.append(task)
    print("Task added!")

def remove_todo():
    task = input("Enter the task to remove: ")
    if task in todos:
        todos.remove(task)
        print("Task removed!")
    else:
        print("Task not found!")

def view_todos():
    print("Your to-do list:")
    for task in todos:
        print(f"- {task}")

while True:
    print("\\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_todo()
    elif choice == '2':
        remove_todo()
    elif choice == '3':
        view_todos()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
