import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time, sleep
from windowcapture import WindowCapture, WindowCapture2
from threading import Thread
from track import Tracker
from forward import Forward
from xaxis import Xaxis
import pydirectinput
import win32gui

sleep(3)
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))



# initialize the WindowCapture class
windowName = 'Minecraft 1.11'   
wincap = WindowCapture(windowName)
wincap2 = WindowCapture2(windowName)
tracker = Tracker()
forward = Forward()
xaxis = Xaxis()

# Set Window desired window size.
hwnd = win32gui.FindWindow(None, windowName)
win32gui.MoveWindow(hwnd, 600, 0, 720, 480, True)
bbox = win32gui.GetWindowRect(hwnd)

#Start threads.
xaxis.start()

pydirectinput.PAUSE = 0.0001



while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    screenshot2 = wincap2.get_screenshot()
    

    #Give these vision video feedback
    tracker.function(screenshot)
    forward.function(screenshot2)

    #Turn these into movement controlls
    xaxis.run(tracker.x_medium,tracker.y_medium)



    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):

        cv.destroyAllWindows()
        break


print('Done.')
