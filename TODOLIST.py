class List:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)
        print("Task added successfully!")
    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")
    def display(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")
def main():
    to_do_list = List()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            task = input("Enter the task to add: ")
            to_do_list.add(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            to_do_list.remove(task)
        elif choice == '3':
            to_do_list.display()
        elif choice == '4':
            print("Exiting the To-Do List application. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
