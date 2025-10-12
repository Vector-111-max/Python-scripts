#Decision maker

#Important : this is thought to fight paralysis analysis in common daily life situations (like deciding on a movie to watch among a lot of movies).
#Don't use this for critical decisions!

#Variables :
#option (input from user)
#options (list)
#op (option's number)

import random

print("Type your options here\nType 'done' when you finish")

options = []
op = 1

while True :

    option = input(f"Option {op} : ")
    if option.lower() == "done" :
        break
    options.append(option)
    op += 1
    

print(random.choice(options))
