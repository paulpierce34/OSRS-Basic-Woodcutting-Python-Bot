import pyautogui
import cv2
import time

pyautogui.FAILSAFE = True

while (1==1):
    time.sleep(8)
    treelocation = pyautogui.locateOnScreen('exact.png', confidence=0.4)
    if (treelocation):
        print (f"{treelocation}")
        pyautogui.moveTo(treelocation, duration=1)
        pyautogui.click()
    else:
        print("None found, moving back to previous location.");
        pyautogui.moveTo(treelocation, duration=1)
        pyautogui.click()
    
        
        


#### Additional pyautogui methods
#pyautogui.moveTo(250, 300, duration=2)
#pyautogui.click()
#pyautogui.PAUSE = 10 ## Pause for 10 seconds
#Take screenshots and save to output file
#im2 = pyautogui.screenshot('output.png')
####

