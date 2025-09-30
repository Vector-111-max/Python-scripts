#Decision maker

#Variables :
#option (input from user)
#options (list)
#op (option's number)

import random

print("Don't know what to do?\nType your options here\nType 'done' when you finish")

options = []
op = 1

while True :

    option = input(f"Option {op} : ")
    if option.lower() == "done" :
        break
    options.append(option)
    op += 1
    
print(random.choice(options))