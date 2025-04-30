import time
lst=[]
while True:
    time.sleep(2)
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        task=input("Enter your task which you want to add: ")

        lst.append(task) 
        print("your to do list is ","\n",lst)
    elif choice ==2:
        print(f"Your task list is {lst}")
        re=input("Enter the task you want to remove: ")
        lst.remove(re)
        if len(lst)==0:
            print("your to do list is empty")
        else:
            print("Your to do list is","\n",lst)
    elif choice ==3:
        print("Thank you")
        break
