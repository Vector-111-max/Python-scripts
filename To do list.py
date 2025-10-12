#Not finished

#To do list
#Note to myself : gotta fix empty string bug

to_do = []
def generate_list():
    print("Type \"done\" when you finish")

    while not any(item.lower() == "done" for item in to_do):
        usr_lst = input("Task: ")
        if usr_lst == "":
            print("Must enter a Task!")
        elif usr_lst in to_do:
            print("Task already in list!") 
            del to_do[-1]
        to_do.append(usr_lst)
    
    if "" in to_do:
        to_do.remove("")
    elif any(item.lower() == "done" for item in to_do):
        del to_do[-1]

def check_list():
     if to_do == []:
         print("No tasks")
     else:
        for i in to_do:
            print(i)
