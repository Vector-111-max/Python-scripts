#Password generator

import pyperclip
import string
import random

characters = list(string.ascii_letters + string.punctuation + string.digits + " ")
password = ""

for i in range(20) :
    i = random.choice(characters)
    password += i

pyperclip.copy(password)
print(password, "\nCopied to clipboard")

