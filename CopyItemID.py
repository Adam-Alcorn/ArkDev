import pyautogui
import time;
time.sleep(10)
for x in range(100):
    pyautogui.FAILSAFE = True
    pyautogui.size()
    pyautogui.click(x=100, y=200, clicks=2, interval=0.3, button='left')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(x=400, y=600, clicks=2, interval=0.3, button='left')
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.locateCenterOnScreen()  # returns center x and y
    pyautogui.click()