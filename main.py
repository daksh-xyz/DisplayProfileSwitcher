# from playsound import playsound
import psutil
import playsound
import pywintypes
import win32api
import win32con
import pyautogui
from time import sleep



def hdrcon():
    if psutil.sensors_battery().power_plugged == True:
        pyautogui.keyDown("win")
        pyautogui.keyDown("alt")
        pyautogui.keyDown("b")
        pyautogui.keyUp("win")
        pyautogui.keyUp("alt")
        pyautogui.keyUp("b")
    elif psutil.sensors_battery().power_plugged == False:
        pyautogui.keyDown("win")
        pyautogui.keyDown("alt")
        pyautogui.keyDown("b")
        pyautogui.keyUp("win")
        pyautogui.keyUp("alt")
        pyautogui.keyUp("b")
    else:
        print('an error occurred')

# def fanspeed():
#     while psutil.sensors_battery().power_plugged == True:
#         if psutil.sensors_fans() < 3000:
#             with pyautogui.hold("fn"):
#                 pyautogui.press("f")
# fanspeed()



def changeres():
    # try:
    if psutil.sensors_battery().power_plugged == True:
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = 2880
        devmode.PelsHeight = 1800
            
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, 0)

    elif psutil.sensors_battery().power_plugged == False:
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = 1920
        devmode.PelsHeight = 1200

        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, 0)


    # except Exception:
    #     print('shit')
    #     exit()

def confirmation_message():
    user_input = input('''
                --------------------------------------------
                         CHANGE SCREEN RESOLUTION
                --------------------------------------------
                Do you want to change screen settings?
                y/n: ''')
    y = input('\n\nDo you want to toggle HDR?: ')
    if y == 'y':
        hdrcon()
    else:
        pass
    if user_input == 'n':
        pass
    elif user_input == 'y':
        sleep(2)
        changeres()
confirmation_message()

def charging_alarm():
    if psutil.sensors_battery().percent == 100:
            playsound.playsound('Alarm04.wav')
    else:
        print('not yet')
charging_alarm()