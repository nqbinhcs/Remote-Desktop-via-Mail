import cv2 
import os
import datetime


class Webcam():
    def __init__(self):
        pass

    def run(self, code, time=10):
        if code == "image":
            return self.screenshot()
        elif code == "video":
            return self.record(time)
         
        return ''

    def screenshot(self):
        try:
            cam = cv2.VideoCapture(0)
            _, img = cam.read()

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).png
            now = datetime.datetime.now()
            filename = str(now.year%100) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '.png'
            
            path = os.path.join('.temp', filename)

            cv2.imwrite(path, img)

            cam.release()

            return filename
        
        except OSError:
            return ''

    def record(self, time):
        try:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 20
            cam = cv2.VideoCapture(0)

            # create file-name according yy-m(m)-d(d)-h(h)-m(m)-s(s).png
            now = datetime.datetime.now()
            filename = str(now.year%100) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '.png'
            
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
