#Not finished

#To do list
#[10/12/25] Note to myself : gotta fix empty string bug (fixed)

to_do = []
def generate_list():
    print("Type \"done\" when you finish")

    while not any(item.lower() == "done" for item in to_do):
        usr_lst = input("Task: ")
        if usr_lst == "":
            print("Must enter a Task!")
            to_do.append(usr_lst)
            to_do.insert(0, "")
            del to_do[-1]
            del to_do[0]
        elif usr_lst in to_do:
            print("Task already in list!") 
        else:
            to_do.append(usr_lst)
    
    if any(item.lower() == "done" for item in to_do):
        del to_do[-1]

def check_list():
     if to_do == []:
         print("No tasks")
     else:
        for i in to_do:
            print(i)

def mark_task():
    pass

def del_task():
    while to_do != []:
        task = input("Delete task: ")  
        if task not in to_do:
            print(f"There's not a task named {task}!")
        elif task in to_do:
            to_do.remove(task)
            print("Task deleted") 
        else:
            print("No tasks!")

#Note to myself: add exception for string and float input
while True: 
    action = int(input("\"1\" to generate list\n\"2\" to check list\n\"4\" to delete a task\n- "))

    if action == 1:
        generate_list()
    elif action == 2:
        check_list()
    #elif action == 3:
    elif action == 4:
        del_task()
    #elif action == 5:
