import cv2
import numpy as np
import os

class VideoWriter:

    def __init__(self, inpath, outpath, size, num_frames, fps):
        self.inpath = inpath
        self.outpath = outpath
        self.size = size
        self.num_frames = num_frames
        self.fps = fps



    def write(self):

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(self.outpath + "/video.mp4",fourcc, self.fps, self.size)
        for i in range(self.num_frames):
            img = cv2.imread(self.inpath + '/img' + str(i) + '.jpg')
            writer.write(img)
        cv2.destroyAllWindows()
        writer.release()
