import numpy as np
from mss import mss
import sys
import time
import cv2


class AutoCapture():

    def __init__(self, interval, duration, path, size):

        self.interval = interval
        self.duration = duration
        self.w, self.h = size
        self.path = path

        self.global_start = time.time()


    def new_construct_window(self):
        bound_box = {'top' : 0, 'left' : 0, 'width' : self.w, 'height' : self.h}
        screenshot = np.array(mss().grab(bound_box))
        return screenshot


    def capture(self):
        counter = 0
        while time.time() - self.global_start < self.duration:
            start = time.time()
            screenshot = self.new_construct_window()
            print(screenshot.shape)
            cv2.imwrite(self.path +  "/img" + str(counter) + ".jpg", screenshot)
            counter += 1
            while time.time()-start < self.interval:
                time.sleep(0.001)
                continue
