import pyautogui as g
import time

def clicked(pos):
    print("clicked at", pos)

screenWidth, screenHeight = g.size()
x, y, = 537, 49
text = ""
pos = g.position()


newTab = "newtabbutton.png"
newTabPos = g.locateCenterOnScreen(newTab)

text = g.prompt(text='Enter URL to type', title='URL input', default='google.com')
time.sleep(1) 
if(newTabPos != None):
    g.click(newTabPos)
    clicked(pos)

    g.click(x, y)
    clicked(pos)

    g.write(text)
    print("typed", text)

    g.keyDown('enter')
    print("pressed enter")

    input()
else:
    print("ERROR: Make sure browser is in view of the screen and not obstructed!")
    input()
    
