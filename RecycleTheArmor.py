import pyautogui
import time;
time.sleep(10)
for x in range(100):
    pyautogui.moveTo(1400, 300)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(900,600)
    pyautogui.doubleClick()

