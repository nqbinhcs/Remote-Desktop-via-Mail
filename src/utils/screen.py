import cv2
import numpy as np
import os
from PIL import ImageGrab
import datetime


class Screen():
    """An class for managing screen
    """

    def __init__(self):
        try:
            os.mkdir('.temp')
        except:
            pass

    def run(self, code, time=10):
        """Capture screen or recording screen
        
        :param code: (str) 'image' or 'video'
        :return: (str) name of a file after executing command
        """
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)
        return ''

    def screenshot(self):
        """Capture screen
        
        :return: name of file screenshot
        """
        try:
            img = ImageGrab.grab()

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).png
            now = datetime.datetime.now()
            filename = str(now.year % 100) + '-' + str(now.month) + '-' + str(now.day) + \
                '-' + str(now.hour) + '-' + str(now.minute) + \
                '-' + str(now.second) + '.png'

            path = os.path.join('.temp', filename)
            img.save(path)
            return filename
        except OSError:
            return ''

    def record(self, time):
        """Record screen in x second(s)
        
        :param time: (int)
        :return: name of file record
        """
        try:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 12

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).avi
            now = datetime.datetime.now()
            filename = str(now.year % 100) + '-' + str(now.month) + '-' + str(now.day) + \
                '-' + str(now.hour) + '-' + str(now.minute) + \
                '-' + str(now.second) + '.avi'

            path = os.path.join('.temp', filename)

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

            return filename

        except OSError:
            return ''
