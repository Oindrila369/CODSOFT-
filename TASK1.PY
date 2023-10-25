empty_list = {}

#add a task
def add_task():
    task = input("Enter a new task: ")
    priority = input("Enter the priority (High, Medium, Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Task not added.")
        return

    empty_list[task] = priority
    print(f"Task '{task}' added with priority '{priority}'.")

#view tasks
def view_tasks():
    if empty_list:
        print("To-Do List:")
        for task, priority in empty_list.items():
            print(f"{task} (Priority: {priority})")
    else:
        print("Your list is empty.")

#update task
def update_task():
    view_tasks()
    task_to_update = input("Enter the task you want to update: ")
    if task_to_update in empty_list:
        new_priority = input("Enter the new priority (High, Medium, Low): ").capitalize()
        if new_priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Task not updated.")
        else:
            empty_list[task_to_update] = new_priority
            print(f"Priority of '{task_to_update}' updated to '{new_priority}'.")
    else:
        print("Task not found in your list.")

#Main loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Priority")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
