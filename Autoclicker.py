#Autoclicker
#Ctrl + C to shut down

import time 
import pyautogui

def autoclicker(interval):
    global click_select 
    while True:
        if click_select.lower() == "left" :
            pyautogui.click()
            time.sleep(interval)
        elif click_select.lower() == "right" :
            pyautogui.rightClick()
            time.sleep(interval)

click_select = input("Select click button (\"Right or Left\"): ")
interval = float(input("Time between clicks: "))
print("Autoclicking...")

autoclicker(interval)
