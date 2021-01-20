import pydirectinput
import cv2 as cv
import numpy as np
from xaxis import Xaxis

xaxis = Xaxis()


class Tracker:
    
    x_medium = 330
    y_medium = 70

    def function(self, putithere):
        
        hsv_frame = cv.cvtColor(putithere, cv.COLOR_BGR2HSV)
        
        low_red  = np.array([0, 60, 0])
        high_red = np.array([20, 200 ,255])
        red_mask = cv.inRange(hsv_frame, low_red, high_red)
        
        contours, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv.boundingRect(cnt)

            #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.x_medium = int((x + x + w) / 2)
            self.y_medium = int((y + y + h) / 2)
            


            break

        

        cv.line(putithere, (self.x_medium, 0), (self.x_medium, 480), (0, 255, 0), 2)
        cv.line(putithere, (0, self.y_medium), (640, self.y_medium), (0, 255, 0), 2)



        cv.imshow("A", putithere)
        cv.imshow("B", red_mask)