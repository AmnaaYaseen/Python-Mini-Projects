import json


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "[✔]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")

    def update_task(self, task_index, new_task):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["task"] = new_task
            self.save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")


def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to update: "))
            new_task = input("Enter new task description: ")
            todo.update_task(index, new_task)
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(index)
        elif choice == "5":
            todo.view_tasks()
            index = int(input("Enter task number to delete: "))
            todo.delete_task(index)
        elif choice == "6":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
