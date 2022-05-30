from textwrap import fill
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ANCHOR, PhotoImage

import src.sender as sender
import src.textstyles as style
import src.themecolors as themecolor

class FileSystem(tk.Frame, sender.Sender):
    def __init__(self, parent, sender):
        tk.Frame.__init__(
            self, parent, bg=themecolor.background)
        
        self.sender = sender

        self.logo = tk.Label(self, text="FileSystem")
        self.logo.pack()

        self.btn_frame = tk.Frame(self, bg=themecolor.background) 
        self.btn_frame.pack(side=tk.LEFT, padx=10)
        
        self.show_frame = tk.Frame(self, bg=themecolor.background)                                        # width=width*2.0/3.0)
        self.show_frame.pack(side=tk.RIGHT)

        self.create_widgets()
    
    def create_widgets(self):
        self.btn_frame.btn_capture = tk.Button(self.btn_frame, text="Capture", command=self.capture)
        self.btn_frame.btn_show_treeview = tk.Button(self.btn_frame, text="show_treeview", command=self.show_treeview)
        self.btn_frame.btn_copy = tk.Button(self.btn_frame, text="copy", command=self.copy)
        self.btn_frame.btn_capture.grid(row=0, column=0, pady=(0, 20))
        self.btn_frame.btn_show_treeview.grid(row=1, column=0, pady=(0, 20))
        self.btn_frame.btn_copy.grid(row=2, column=0)

        # Area for showing image/video 
        # .... 
        # ...

        # example

        cols = ("col1", "col2", "col3")
        self.show_frame.treeview = ttk.Treeview(self.show_frame, columns=cols, show="headings")
        self.show_frame.treeview.pack(side=tk.LEFT, fill="both",expand=True)
        scrollbar = ttk.Scrollbar(self.show_frame, orient=tk.VERTICAL, command=self.show_frame.treeview.yview)
        self.show_frame.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill="both")
        #
    
    def capture(self):
        subject = "capture"
        body = "capture please"

        # self.sender.send_mail(["nguyenhieu82132@gmail.com"], subject, body)

    def show_treeview(self):
        # Show len cai email
        print()

    def copy(self):
        subject = "copy"
        body = "copy please"

        # self.sender.send_mail(["nguyenhieu82132@gmail.com"], subject, body)

