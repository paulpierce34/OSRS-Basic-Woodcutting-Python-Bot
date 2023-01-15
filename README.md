# OSRS-Basic-Woodcutting-Python-Bot
This is an extremely basic python script that uses the pyautogui library to cut trees for you in old school runescape. This same concept can realistically be applied to almost any sort of grinding mechanism in runescape. Essentailly, you feed a screenshot of the item (in this case, a tree) to the script and the script looks for this item on your screen to click on it. 

Please feel free to steal my concepts if they spark any ideas for you and run with them! 

NOTE: You can tweak the confidence level of the image in the script if you want more/less accuracy, change the screenshot, sleep timer, etc. In my opinion this is a super portable foundational start conceptually to a script that can automate a lot of things in runescape.

An immediate change I'd like to make would be to have a bunch of different pictures of trees, iterate through them in a for loop, and if true go click on them and cut them down. As opposed to the one screenshot I have right now... which is still semi-accurate, but not as good as it can be. Anyways, I will be making constant iterations to this repository whenever I get time!

Requirements:
- Python 3 (I am using version 3.10.9)
- pyautogui (pip install pyautogui)
- Opencv (pip install opencv-python)
- time (you probably already have this)

HOW TO USE:
- Open a terminal (cmd prompt or powershell)
- cd to the directory where you have the python script located
- execute script by typing 'python3 woodCutter.py'

Proof of concept:
https://youtu.be/9LXMtTYb2Jc
