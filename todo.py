class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"✓ Task added: '{description}'")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks in your to-do list.")
            return
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print()

    def mark_task_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].done = True
            print(f"✓ Task '{self.tasks[index - 1].description}' marked as done.")
        else:
            print("❌ Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"✓ Task deleted: '{removed.description}'")
        else:
            print("❌ Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n=== TO-DO LIST APP ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                index = int(input("Enter task number to mark as done: "))
                todo.mark_task_done(index)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            todo.view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                todo.delete_task(index)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()