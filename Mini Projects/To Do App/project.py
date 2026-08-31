tasks = []

while True:

    print("/n1.Add Task: ")
    print("2.View Task: ")
    print("3.Delete Task: ")
    print("4.Exit: ")

    choice = input("Please Enter Choice: ")

    if choice == "1":
        task = input("Enter a new Task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks,1):
            print(i,task)

    elif choice == "3":
        num = int(input("Enter Task Number: "))
        if 1 <= num <= len(tasks):
            
            tasks.pop(num -1)
            print("Task Deleted!")

        
    elif choice == "4":
        break

        print("Exit Successfully!")

    else:
        print("Invalid Task Number!")

