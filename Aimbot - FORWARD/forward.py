import pydirectinput
import cv2 as cv
import numpy as np
from xaxis import Xaxis
import pydirectinput

class Forward:
    
    leftX = 0
    rightX = 0
    x_medium = 0
    y_medium = 0
    size = 2
    x = 0
    color = 0

    def function(self, putithere):
        
        hsv_frame = cv.cvtColor(putithere, cv.COLOR_BGR2HSV)
        
        low_red  = np.array([0, 60, 0])
        high_red = np.array([20, 200 ,255])
        red_mask = cv.inRange(hsv_frame, low_red, high_red)
        
        contours, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse=True)

        #Draw contours
        cv.drawContours(putithere, contours, -1, (0,255,0),1)

        for cnt in contours:
            (x, y, w, h) = cv.boundingRect(cnt)

            self.leftX = int(x)
            self.rightX = int(x + w)

            cv.rectangle(putithere, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.line(putithere, (x, y), (x + w, y + h), (0, 255, 0), 2)

            break
        
   
        
        if not contours:
            pydirectinput.keyUp("w") #If theres none, do not do anything.
            self.color = 0
            self.leftX = 296
            self.rightX = 296
        elif self.leftX > 74 and self.rightX < 518:  #Kepep going
            self.color = 255
            pydirectinput.keyDown("w")
            pydirectinput.mouseDown()
        elif self.leftX < 74 and self.rightX > 518: #Desired place
            self.color = 0
            pydirectinput.keyUp("w")
            pydirectinput.mouseUp()
            
            


        #Left Side
        #cv.line(putithere,  (self.leftX, 32),    (self.leftX, 197),     (0, 0, 255), 4)
        #Right Side
        #cv.line(putithere,  (self.rightX, 32),    (self.rightX, 197),     (0, 0, 255), 4)
        
        cv.line(putithere,  (74, 32),    (74, 197),     (0, 0, self.color), 4)
        cv.line(putithere,  (518, 32),    (518, 197),   (0, 0, self.color), 2)

        cv.imshow("AA", putithere)
        cv.imshow("AB", red_mask)