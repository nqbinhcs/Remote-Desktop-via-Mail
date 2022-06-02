import cv2  # pip install opencv-python
import numpy as np
from PIL import ImageGrab
from PIL import Image, ImageTk
import os


class Webcam():
    def __init__(self):
        self.flag = False
        self.width = 0
        self.height = 0
        pass

    def run(self, code, time=10):
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)

    def screenshot(self):
        cam = cv2.VideoCapture(0)
        res, img = cam.read()

        path = os.path.join('.temp', 'webcam.png')

        cv2.imwrite(path, img)

        # Get width & height of image capturing from webcam
        if self.flag == False:
            img = Image.open(path)
            self.width = img.width
            self.height = img.height
            self.flag = True

        cam.release()

    def record(self, time):
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        fps = 20
        cam = cv2.VideoCapture(0)

        path = os.path.join('.temp', 'webcam-record.avi')

        if self.flag:
            out = cv2.VideoWriter(path, fourcc, fps, (self.width, self.height))

        for i in range(time*fps):
            res, img = cam.read()

            if self.flag == False:
                cv2.imwrite("webcam.png", img)
                image = Image.open("webcam.png")
                self.width = image.width
                self.height = image.height
                self.flag = True
                out = cv2.VideoWriter(
                    "output.avi", fourcc, fps, (self.width, self.height))

                os.remove("webcam.png")

            out.write(img)
            cv2.waitKey(1)

        cam.release()
        out.release()
