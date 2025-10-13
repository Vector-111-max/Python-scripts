#Not finished
#To do list
#[12/10/25] Note to myself : gotta fix empty string bug (fixed)
#[13/10/2025] Note to myself : fix bug in mark_task function (it won't mark the last task in the list)

to_do = []
def generate_list(): #Asks constant input from the user until indicated to stop. Then appends it to the to_do list
    print("Type \"done\" when you finish")

    while not any(item.lower() == "done" for item in to_do): #Starts the loop and constantly checks if the word "done" has been submitted. It's also case insensitive
        usr_lst = input("Task: ")
        if usr_lst == "":
            print("Must enter a Task!")
        elif usr_lst in to_do:
            print("Task already in list!") 
        else:
            to_do.append(usr_lst)
    
    if any(item.lower() == "done" for item in to_do): #Deletes the word "done" from the list 
        del to_do[-1]

def check_list(): #prints to_do list in descending format
     if to_do == []:
         print("No tasks") #Just a reminder in case the list is empty
     else:
        for i in to_do:
            print(i)

def mark_task(): #Marks a task as done
    mark = input("Select a task: ")
    if mark in to_do:
        for i in range(0, len(to_do) - 1):
            if to_do[i] == mark :
                to_do[i] = "✓" + mark

def del_task():
    if to_do == []:
        print("No tasks!")
    while to_do != []:
        task = input("Delete task: ")  
        if task.lower() == "done":
            break
        elif task not in to_do:
            print(f"There's not a task named {task}!") 
        else:
            to_do.remove(task)
            print("Task deleted")
            if to_do == []:
                print("All tasks deleted")

while True: 
    try:
        action = int(input("\"1\" to generate list\n\"2\" to check list\n\"4\" to delete a task\n- "))

        if action == 1:
            generate_list()
        elif action == 2:
            check_list()
        elif action == 3:
            mark_task()
        elif action == 4:
            del_task()
        elif action == 5:
            break
        else:
            print("Must enter a valid option")
    except ValueError:
        print("Must enter a valid option")
