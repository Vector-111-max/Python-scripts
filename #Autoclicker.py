#Autoclicker

import time 
import pyautogui

def autoclicker(interval):
    while True:
        pyautogui.click()
        time.sleep(interval)

interval = float(input("Time between clicks: "))

autoclicker(interval)