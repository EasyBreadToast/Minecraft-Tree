import cv2 as cv
from threading import Thread, Lock
import pydirectinput

class Xaxis:

    #Set pydirectinput delay:
    pydirectinput.PAUSE = 0.01

    # threading properties
    stopped = True
    lock = None


    def __init__(self):
        # create a thread lock object
        self.lock = Lock()


    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self,xvalue,yvalue):

        xaxies = xvalue
        yaxies = yvalue

        print(xaxies,yaxies)

        if xaxies > 340:
            pydirectinput.move(1,0)
            pydirectinput.move(2,0)
        else:
            pass

        if xaxies < 320:
            pydirectinput.move(-1,0)
            pydirectinput.move(-2,0)
        else:
            pass          


        pass