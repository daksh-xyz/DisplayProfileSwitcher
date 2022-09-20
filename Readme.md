# Display Profile Switcher
## or DPS
</br>

### WHAT IT DOES:
Well basically, "toggles" HDR and then changes screen resolution depending on power state  
for example:  
1. On plugging into AC power the script asks user if he wants to switch display profiles if yes then:  
"toggles" HDR and after a delay changes screen resolution to 2880 x 1800  
otherwise:  
exits console window  
2. On switching to battery power the script asks user if he wants to switch display profiles if yes then:  
"toggles" HDR and after a delay changes screen resolution to 1920 x 1200  
Otherwise:  
exit console window

## HOW TO GET IT TO WORK?
Requires libraries listed below:  

<code> 1. import psutil  </code><br>
<code> 2. import playsound  </code><br>
<code> 3. import pywintypes  </code><br>
<code> 4. import win32api  </code><br>
<code> 5. import win32con  </code><br>
<code> 6. import pyautogui  </code><br>
<code> 7. from time import sleep  </code><br>


Additional work required to get it to run the python script ASA charger gets plugged in.  
To do that:  
1. Launch Task Scheduler 
1. Click on create a Task
1. Enter a custom name for your task
1. Go to Actions tab on the top,
1. Click on New on the bottom left
1. Under settings in the program/script section enter your python.exe path which would something like this:  
<code>C:\Users\UserName\AppData\Local\Programs\Python\Python310\python.exe</code>  

1. In the &nbsp;<code>"Add arguments"</code>&nbsp; field enter the name of the file in this case:  
<code>main.py</code>

1. In the &nbsp;<code>"Start In"</code>&nbsp; field enter the PATH of the FOLDER where &nbsp;<code>"main.py"</code>&nbsp; is present
1. UNCHECK ALL CONDITIONS from &nbsp;<code>"conditions"</code>&nbsp; tab to prevent any errors.
1. ## SETTING A TRIGGER TO EXECUTE A FILE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THIS IS A LAGGY PART!  
1. Click on TRIGGERS tab
2. Click on New
1. In Begin a task:  
Click on the drop down menu and select &nbsp;<code>"ON AN EVENT"</code>&nbsp;  
In the log field:  
&nbsp;&nbsp;&nbsp;scroll down to the end and select &nbsp;<code>"System"&nbsp;</code>  
In the Source field:  
&nbsp;&nbsp;&nbsp;scroll down to find &nbsp;<code>"Kernel-Power"&nbsp;</code>  
In the event ID:  
&nbsp;&nbsp;&nbsp;Enter &nbsp;<code>"105"&nbsp;</code>

## ET VOILA IT SHOULD NOW WORK WHEN YOU PLUG INN YOUR LAPTOP(OR PLUG IT OUT) 
<br>
<br>

# THOUGHT BEHIND PROJECT:
1. Mainly because I'm lazy and don't want to do this task again and again
1. Also because this is my first project and it's unique cuz nobody on the internet seemed to have done this before so it is an opprtunity to upload as a first-ever project .
1. Plus I'm bored
<br>
<br>

# FUTURE ASPECTS:
well, since I don't want to kill my brand new laptop and I don't know what some modules can do to my system I'm not implementing a feature to:  
1. Control Fan speed (I do know how tho but, psutil does not support fan sensors for windows yet, so. . . . . . . . bummer)
2. Change refresh rate could not find a single question on stack about this + could not find a command line to change refresh rate, apparently windows does not log this and is unable to change this without installing some shady 3rd party software. . . so, not doing that either lol

NOTE :  
 this could all be solved by me learning and reading or getting WMI documentation but it is too long and couldn't find relevant information on reading/changing refresh rate and fan speed

<br>
<br>

# BONUS FEATURE:
Rings an alarm for 4 seconds when battery is fully charged