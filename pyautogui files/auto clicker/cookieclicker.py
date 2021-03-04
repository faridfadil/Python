import pyautogui as g
import keyboard
import time

imageInput = input("Image name to scan: ").strip()
imagePos = g.locateCenterOnScreen(str(imageInput))


def successLog(image, position):
    print("SUCCESS: ", image, "found at", position)

def clickLog(image, position):
    print(image, "clicked at", position)

def failLog(image):
    print("ERROR: ", image, "not found on screen.")

print("Program calibrating...")
time.sleep(2)




TERMINATE_KEY = "q"

if(imagePos != None):
    successLog(imageInput, imagePos)

    #MAIN LOOP
    while keyboard.is_pressed(TERMINATE_KEY) == False:
       
        g.click(imagePos)
        clickLog(imageInput, imagePos)
    print("Program Terminated")
    input()
        
else:
    failLog(imageInput)
    input()




