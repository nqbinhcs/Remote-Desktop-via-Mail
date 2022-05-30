
import time
from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import HORIZONTAL, ttk
from tkinter import PhotoImage

import src.textstyles as style
import src.themecolors as themecolor
import src.sender as sender
import src.utils as utils

class Process(tk.Frame, sender.Sender):
    def __init__(self, parent, sender):
        tk.Frame.__init__(
            self, parent, bg=themecolor.background)
        
        self.sender = sender

        self.logo = tk.Label(self, text="All applications")
        self.logo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.btn_frame = tk.Frame(self, bg=themecolor.background) 
        self.btn_frame.grid(row=1, column=0, padx=(0, 50))
        
        self.table_frame = tk.Frame(self, bg=themecolor.background)                                        # width=width*2.0/3.0)
        self.table_frame.grid(row=1, column=1)

        self.create_widgets()

    
    def create_widgets(self):
        self.create_icons()

        self.refresh()

        self.btn_frame.btn_refresh = tk.Button(self.btn_frame, image=self.icons['refresh'], bd=0,
                                                    bg=themecolor.background, activebackground=themecolor.background,
                                                    command = self.refresh)
        self.btn_frame.btn_refresh.grid(row=0, column=1, columnspan=2, pady=(0, 20))

        self.btn_frame.btn_kill = tk.Button(self.btn_frame, image=self.icons['kill'], bd=0,
                                                    bg=themecolor.background, activebackground=themecolor.background,
                                                    command = self.kill)
        self.btn_frame.btn_kill.grid(row=1, column=1, columnspan=2)

        # table:
        cols = ("Name", "ID", "Count thread")
        self.table_frame.table = ttk.Treeview(self.table_frame, columns=cols, show="headings")
        self.table_frame.table.pack(side=tk.LEFT, fill="both",expand=True)
        scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.table_frame.table.yview)
        self.table_frame.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill="both")
        
        # add column values ...
        # get values from responded email after calling self.refresh() 
        # show the values in treeview ...

        
    def create_icons(self):
        self.icons = {}
        self.icons['logo'] = ImageTk.PhotoImage(
            Image.open('assets/all_app/logo.png').resize((300, 150), Image.ANTIALIAS))
        self.icons['refresh'] = ImageTk.PhotoImage(
            Image.open('assets/all_app/refresh.png').resize((150, 75), Image.ANTIALIAS))
        self.icons['kill'] = ImageTk.PhotoImage(
            Image.open('assets/all_app/kill.png').resize((150, 75), Image.ANTIALIAS))

    def refresh(self):
        subject = 'refresh'
        body = 'refresh please'

        # self.sender.send_mail(["nguyenhieu82132@gmail.com"], subject, body)


    def kill(self):
        subject = 'kill'
        body = 'kill please'

        # self.sender.send_mail(["nguyenhieu82132@gmail.com"], subject, body)

    def back_to_menu(self):
        self.destroy()
        
        