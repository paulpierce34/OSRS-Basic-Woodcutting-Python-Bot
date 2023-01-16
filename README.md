# OSRS-Basic-Woodcutting-Python-Bot
  This is a basic python script that uses the pyautogui library to cut trees for you in old school runescape. This same concept can realistically be applied to almost any sort of grinding mechanism in runescape. Essentailly, you feed a screenshot of the item (in this case, a tree) to the script and the script looks for this item on your screen to click on it. There is an array of screenshots provided in this repository the script looks to match. Please feel free to plug/play your own screenshots.

Please feel free to use my concepts if they spark any ideas for you and run with them! 

NOTE: You can tweak the confidence level of the image in the script if you want more/less accuracy, change the screenshot, sleep timer, etc. In my opinion this is a super portable foundational start conceptually to a script that can automate a lot of things in runescape.

Check out the pyautogui documentation here: https://pyautogui.readthedocs.io/en/latest/

**Limitations:**
- Only officially supports regular logs (but I do recommend replacing screenshot with other types of trees if you wanted to test)
- No ability to deposit into bank yet

**Requirements (included in requirements.txt file for easy use):**
- Python 3 (I am using version 3.10.9)
- pyautogui (pip install pyautogui)
- Opencv (pip install opencv-python)
- time (you probably already have this)

**HOW TO USE:**
- Open a terminal (cmd prompt or powershell)
- cd to the directory where you have the python script located
- Type the command: 'pip install -r requirements.txt'  to install all python reqs
- execute script by typing 'python3 woodCutter.py'

**Proof of concept:**
https://youtu.be/9LXMtTYb2Jc

Image used currently (included in repo):

![exact](https://user-images.githubusercontent.com/33561650/212556907-d7e15abb-bd1d-463b-b120-50ee4e64792b.PNG)

Best area for script as of version 1 (and the only area I mainly tested in; Circled in red):
![maps](https://user-images.githubusercontent.com/33561650/212736826-99720282-0a0c-4a93-9cf5-6bd2fb9ddc6d.PNG)


Screenshot of script usage:
![Capture3](https://user-images.githubusercontent.com/33561650/212556945-9860b6ba-6a80-42ab-88b6-ef17cc4b2503.PNG)

