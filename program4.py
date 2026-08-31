#Question 4: Interactive Command-Line Task Scheduler with Lazy Evaluation

tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Run Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        condition = input("Should the task run? (yes/no): ").lower()

        if condition == "yes":
            tasks.append(task)
            print("Task added successfully.")
        elif condition == "no":
            print("Task was not added.")
        else:
            print("Invalid condition.")

    elif choice == "2":
        if tasks:
            print("\nScheduled Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)
        else:
            print("No tasks scheduled.")

    elif choice == "3":
        if tasks:
            print("\nRunning Tasks:")
            while tasks:
                task = tasks.pop(0)
                print("Executing:", task)
        else:
            print("No tasks to run.")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Please try again.")