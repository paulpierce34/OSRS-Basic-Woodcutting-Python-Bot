import pyautogui
import cv2
import time

pyautogui.FAILSAFE = True ## This allows you to move your mouse to upper lefthand corner of your screen as far as possible to cancel script. Refer to pyautogui docs

while (1==1):
    time.sleep(8) ## Sleep for 8 secs
    treelocation = pyautogui.locateOnScreen('exact.png', confidence=0.4) ## Locate the tree you are looking for. Replace image with Yew, Magic, Oak, etc. if need be
    if (treelocation):
        print (f"{treelocation}") ## Print the tree location for user
        pyautogui.moveTo(treelocation, duration=1) ## Move to tree location. NOTE: You can change the duration to move mouse faster/slower
        pyautogui.click() ## Click on the tree you found
    else:
        print("None found, moving back to previous location."); 
        pyautogui.moveTo(treelocation, duration=1) ## Nothing found I'm gonna move in the same direction as previous
        pyautogui.click() ## Click
    
        
        


#### Additional pyautogui methods
#pyautogui.moveTo(250, 300, duration=2)
#pyautogui.click()
#pyautogui.PAUSE = 10 ## Pause for 10 seconds
#Take screenshots and save to output file
#im2 = pyautogui.screenshot('output.png')
####

