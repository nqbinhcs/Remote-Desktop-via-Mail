import cv2
import os
import datetime


class Webcam():
    """An class for managing webcam
    """

    def __init__(self):
        try:
            os.mkdir('.temp')
        except:
            pass

    def run(self, code, time=10):
        """Shot a photo or filming

        :param code: (str) 'image' or 'video'
        :return: (str) name of a file after executing command
        """
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)

        return ''

    def screenshot(self):
        """Shot a photo

        :return: name of file screenshot
        """
        try:
            cam = cv2.VideoCapture(0)
            _, img = cam.read()

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).png
            now = datetime.datetime.now()
            filename = str(now.year % 100) + '-' + str(now.month) + '-' + str(now.day) + \
                '-' + str(now.hour) + '-' + str(now.minute) + \
                '-' + str(now.second) + '.png'

            path = os.path.join('.temp', filename)

            cv2.imwrite(path, img)

            cam.release()

            return filename

        except OSError:
            return ''

    def record(self, time):
        """Filming in x second(s)

        :param time: (int)
        :return: name of file record
        """
        try:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 20
            cam = cv2.VideoCapture(0)

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).png
            now = datetime.datetime.now()
            filename = str(now.year % 100) + '-' + str(now.month) + '-' + str(now.day) + \
                '-' + str(now.hour) + '-' + str(now.minute) + \
                '-' + str(now.second) + '.avi'

            path = os.path.join('.temp', filename)

            _, img = cam.read()
            height, width, _ = img.shape
            out = cv2.VideoWriter(path, fourcc, fps, (width, height))

            for i in range(time*fps):
                _, img = cam.read()
                out.write(img)
                cv2.waitKey(1)

            cam.release()
            out.release()

            return filename

        except OSError:
            return ''
