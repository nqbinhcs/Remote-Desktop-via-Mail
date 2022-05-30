
from src.frames.menu import Menu
from src.frames.process import Process
from src.frames.screen import Screen
from src.frames.webcam import Webcam
from src.frames.keystroke import Keylogger
from src.frames.registry import Registry
from src.frames.fileSystem import FileSystem
import src.sender as sender

from PIL import Image, ImageTk
import tkinter as tk
import src.textstyles as textstyle
import src.themecolors as themecolor
import src.utils as utils
import time
 
ACT_APPLICATION = 'application' 
ACT_SCREEN = 'screen'
ACT_KEYLOGGER = 'keylogger'
ACT_REGISTRY = 'registry'
ACT_FILESYSTEM = 'fileSystem'
ACT_WEBCAM = 'webcam'

class RootView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Config window shape
        self.geometry("1080x720+0+0")
        self.resizable(0, 0)
        self.title('Program')
        self.config(bg=themecolor.background)
        self.grid()

        # SMTP
        self.sender = sender.Sender()

        # Header
        self.head = tk.Frame(self, bg=themecolor.background)
        self.head.pack(expand=False, pady=(75))

        # Body
        self.body = tk.Frame(self, bg=themecolor.background)
        self.body.pack(side=tk.TOP)

        # Objects
        self.menu = None
        self.activity = None

        # Create widgets
        self.create_icons()
        self.create_header()
        self.create_menu()
        self.bind_action()

    def create_sprite(self, path):
        image = Image.open(path)
        image.mode = 'RGBA'
        return ImageTk.PhotoImage(image)

    def run(self):
        self.menu.tkraise()
        self.mainloop()

    def create_icons(self):
        self.icons = {}
        self.icons['back'] = self.create_sprite('assets/menu/back.png')

    def create_header(self):
        # Logo or something
        self.header_img = ImageTk.PhotoImage(file='assets/menu/logo.png')
        self.head.logo = tk.Label(self.head, image=self.header_img, bg=themecolor.background)
        self.head.logo.grid(row=0, column=0, columnspan=2)
        self.btn_back = tk.Button(
            self.head, text="Back", image=self.icons['back'], bd=0,
            width=50, height=50, bg=themecolor.background)
        self.btn_back.grid(row=1, column=0, sticky=tk.W, padx=(0, 50))
    
    def create_menu(self):
        # Create button 
        temp = Menu(parent=self.body)
        temp.grid(row=0, column=0, sticky=tk.W+tk.S+tk.E+tk.N)
        self.menu = temp
        self.btn_back.grid_remove()
        
    def create_activity(self, activity):
        self.btn_back.grid()
        self.title(activity)
        if activity == ACT_APPLICATION:
            self.activity = Process(parent=self.body, sender=self.sender)          
        elif activity == ACT_SCREEN:
            self.activity = Screen(parent=self.body, sender=self.sender)
        elif activity == ACT_KEYLOGGER:
            self.activity = Keylogger(parent=self.body, sender=self.sender)
        elif activity == ACT_REGISTRY:
            self.activity = Registry(parent=self.body, sender=self.sender)  
        elif activity == ACT_FILESYSTEM:
            self.activity = FileSystem(parent=self.body, sender=self.sender)   
        elif activity == ACT_WEBCAM:
            self.activity = Webcam(parent=self.body, sender=self.sender) 
        
        self.activity.grid(row=0, column=0, sticky="nsew")
        self.activity.tkraise()

    def bind_action(self):
        self.menu.btn_listApp['command'] = lambda: self.create_activity("application")
        self.menu.btn_screen['command'] = lambda: self.create_activity("screen")
        self.menu.btn_webcam['command'] = lambda: self.create_activity("webcam")
        self.menu.btn_keylogger['command'] = lambda: self.create_activity("keylogger")
        self.menu.btn_registry['command'] = lambda: self.create_activity("registry")
        self.menu.btn_fileSystem['command'] = lambda: self.create_activity("fileSystem")
        self.menu.btn_shutdown['command'] = self.shutdown
        self.menu.btn_restart['command'] = self.restart
        self.menu.btn_runFromStartup['command'] = self.runFromStartup
        self.menu.btn_information['command'] = self.information
        self.btn_back['command'] = self.back_to_menu

    def shutdown(self):
        subject = 'shutdown b1tch'
        body = "shutdown please"

        # self.server.send_message("nguyenhieu82132@gmail.com", self.server.create_msg(subject, body))

    def restart(self):
        subject = 'restart b1tch'
        body = "restart please"

        # self.server.send_message("nguyenhieu82132@gmail.com", self.server.create_msg(subject, body))

    def runFromStartup(self):
        subject = 'runFromStartup b1tch'
        body = "runFromStartup please"

        # self.server.send_message("nguyenhieu82132@gmail.com", self.server.create_msg(subject, body))

    def information(self):
        print()
        # our information ? student id , email ? ...


    def back_to_menu(self):
        self.activity.destroy()
        self.menu.tkraise()
        self.title('Computer Network Project')
        self.btn_back.grid_remove()
        exit
        


