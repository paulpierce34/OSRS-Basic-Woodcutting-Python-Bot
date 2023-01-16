import pyautogui
import cv2
import time
import re

pyautogui.FAILSAFE = True

## Replace images of trees here if looking for something else other than regular trees
allTrees = ["exact.png", "exact2.png", "exact3.png", "exact4.png", "exact5.png", "pinetree.png", "leaves.png"]

count = 0
while (1==1):
    for treepic in allTrees:
        print(f"Looking for {treepic}")
        treelocation = pyautogui.locateOnScreen(treepic, confidence=0.4) ## Adjust confidence level of images (Valid entries: 0-1)
        if (treelocation):
            print (f"{treelocation}")
            centeroftree = pyautogui.center(treelocation)
            pyautogui.moveTo(centeroftree, duration=1)
            pyautogui.click()
            time.sleep(10)
            break ## Break out of for loop so we restart the process and begin searching for first pic in array
        else:
            print("None found, searching and waiting for more.. moving eventually")
            time.sleep(2) ## sleep 2 secs in between looking for trees to account for trees that respawn
            if (count > 3):
                pyautogui.moveTo(treelocation, duration=1)
                pyautogui.click()
                count = 0
            count += 1
    
        
        


#### Additional pyautogui methods
#pyautogui.moveTo(250, 300, duration=2)
#pyautogui.click()
#pyautogui.PAUSE = 10 ## Pause for 10 seconds
#Take screenshots and save to output file
#im2 = pyautogui.screenshot('output.png')
####

## LATER - try to inverse current location of tree and move to that when none are found. Essentially moves character back towards where tree was initially:
#TreeLocationString = str(treelocation)
#print(re.sub('[1-9][1-9][1-9]', 'yo', TreeLocationString)) ; instead of replacing with yo, just append a '-' to number. then we can click to that mouse location. Problem is idk how to do this in python, when I try '\1' it does not work
