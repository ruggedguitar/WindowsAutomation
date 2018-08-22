import pyautogui
import subprocess
import time

def OpenUpdates():
    subprocess.call('C:\Windows\System32\control.exe')

def CheckUpdate():
    pyautogui.typewrite("Windows Update")
    time.sleep(1)
    pyautogui.click(115, 86)
    time.sleep(1)
    pyautogui.click(75, 116)

def MaxWin():
    pyautogui.keyDown('alt')
    pyautogui.press(' ')
    pyautogui.press('x')
    pyautogui.keyUp('alt')

def Center():
    pyautogui.click(960, 540)

OpenUpdates()
time.sleep(1)
MaxWin()
CheckUpdate()
Center()
