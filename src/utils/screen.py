import cv2  # pip install opencv-python
import numpy as np
import os
from PIL import ImageGrab
from PIL import Image, ImageTk


class Screen():
    def __init__(self):
        img = ImageGrab.grab()
        self.height = img.height
        self.width = img.width
        pass

    def run(self, code, time=10):
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)

    def screenshot(self):
        img = ImageGrab.grab()
        # print('----')
        path = os.path.join('.temp', 'screenshot.png')
        img.save(path)

    def record(self, time):
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        fps = 12

        path = os.path.join('.temp', 'screen-record.avi')

        out = cv2.VideoWriter(path, fourcc, fps,
                              (self.width, self.height))

        # fps = 12 -> 12 images / second
        #     ==> Just grab() 12 times
        for i in range(int(time * fps)):
            img = ImageGrab.grab()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.waitKey(1)

        out.release()
