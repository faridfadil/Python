import pyautogui as g
import time as t

delay = 0.6

def openApp(name):
    g.press('win')
    g.write(name)
    g.press('enter')

print('Opening PomoDoneApp')
openApp('pomodoneapp')
t.sleep(delay)
print('Opening Brave')
openApp('brave')
