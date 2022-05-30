# import PIL
from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import PhotoImage

import src.textstyles as style
import src.themecolors as themecolor


class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(
            self, parent, bg=themecolor.background)
        self.feature_height = 75
        self.feature_width = 150
        self.create_widgets()

    def create_icons(self):
        self.icons = {}

        self.icons['app'] = ImageTk.PhotoImage(
            Image.open('assets/menu/listApp.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))

        self.icons['screen'] = ImageTk.PhotoImage(
            Image.open('assets/menu/screen.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['shutdown'] = ImageTk.PhotoImage(
            Image.open('assets/menu/shutdown.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['restart'] = ImageTk.PhotoImage(
            Image.open('assets/menu/restart.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['keylogger'] = ImageTk.PhotoImage(
            Image.open('assets/menu/keylogger.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['registry'] = ImageTk.PhotoImage(
            Image.open('assets/menu/registry.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['fileSystem'] = ImageTk.PhotoImage(
            Image.open('assets/menu/fileSystem.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['runFromStartup'] = ImageTk.PhotoImage(
            Image.open('assets/menu/runFromStartup.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
        
        self.icons['webcam'] = ImageTk.PhotoImage(
            Image.open('assets/menu/webcam.png').resize((self.feature_width, self.feature_height), Image.ANTIALIAS))
            
        self.icons['information'] = ImageTk.PhotoImage(
            Image.open('assets/menu/information.png').resize((149, 24), Image.ANTIALIAS))

    def create_sprite(self, path):
        image = Image.open(path)
        image.mode = 'RGBA'
        return ImageTk.PhotoImage(image)

    def create_widgets(self):
        self.create_icons()

        '''row 1'''
        # List all processes
        self.btn_listApp = tk.Button(
            self, image=self.icons['app'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_listApp.grid(row=0, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_listApp.config(height=self.feature_height, width=self.feature_width)

        # Screen: {Capture, Record}
        self.btn_screen = tk.Button(
            self, image=self.icons['screen'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_screen.grid(row=0, column=1, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_screen.config(height=self.feature_height, width=self.feature_width)
        
        # Webcom: {Capture, Record}
        self.btn_webcam = tk.Button(
            self, image=self.icons['webcam'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_webcam.grid(row=0, column=2, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_webcam.config(height=self.feature_height, width=self.feature_width)

        '''row 2'''
        # Key logger
        self.btn_keylogger = tk.Button(
            self, image=self.icons['keylogger'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_keylogger.grid(row=2, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_keylogger.config(height=self.feature_height, width=self.feature_width)
        
        # Write on registry
        self.btn_registry = tk.Button(
            self, image=self.icons['registry'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_registry.grid(row=2, column=1, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_registry.config(height=self.feature_height, width=self.feature_width)
        
        # File system: copy file(s)
        self.btn_fileSystem = tk.Button(
            self, image=self.icons['fileSystem'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_fileSystem.grid(row=2, column=2, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_fileSystem.config(height=self.feature_height, width=self.feature_width)

        '''row 3'''
        # Shutdown
        self.btn_shutdown = tk.Button(
            self, image=self.icons['shutdown'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_shutdown.grid(row=4, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_shutdown.config(height=self.feature_height, width=self.feature_width)
        
        # Restart
        self.btn_restart = tk.Button(
            self, image=self.icons['restart'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_restart.grid(row=4, column=1, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_restart.config(height=self.feature_height, width=self.feature_width)
        
        # Set the program 'run from startup'
        self.btn_runFromStartup = tk.Button(
            self, image=self.icons['runFromStartup'], cursor="hand2", borderwidth=0, 
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_runFromStartup.grid(row=4, column=2, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, rowspan=2)
        self.btn_runFromStartup.config(height=self.feature_height, width=self.feature_width)
        
        '''row 4'''
        # Information
        self.btn_information = tk.Button(
            self, image=self.icons['information'], cursor="hand2", borderwidth=0,
            bg=themecolor.background,
            activebackground=themecolor.background)
        self.btn_information.grid(row=6, column=1, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=20)
        self.btn_information.config(height=24, width=149)
