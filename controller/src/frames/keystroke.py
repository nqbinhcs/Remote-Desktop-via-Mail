from textwrap import fill
from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ANCHOR, PhotoImage

import src.sender as sender
import src.textstyles as style
import src.themecolors as themecolor

class Keylogger(tk.Frame, sender.Sender):
    def __init__(self, parent, sender):
        tk.Frame.__init__(
            self, parent, bg=themecolor.background)
        
        self.sender = sender

        self.logo = tk.Label(self, text="Key logger")
        self.logo.pack()

        self.btn_frame = tk.Frame(self, bg=themecolor.background) 
        self.btn_frame.pack(side=tk.LEFT)
        
        self.show_frame = tk.Frame(self, bg=themecolor.background)                                        # width=width*2.0/3.0)
        self.show_frame.pack(side=tk.RIGHT)

        self.create_widgets()
    
    def create_widgets(self):
        self.btn_frame.btn_capture = tk.Button(self.btn_frame, text="Capture", command=self.capture)
        self.btn_frame.btn_show = tk.Button(self.btn_frame, text="Show", command=self.show)
        self.btn_frame.btn_capture.grid(row=0, column=0, pady=(0, 20))
        self.btn_frame.btn_show.grid(row=1, column=0)

        # Area for showing image/video 
        # .... 
        # ...

        # example

        self.show_frame.image = tk.Text(self.show_frame, height=10, width=50)
        self.show_frame.image.pack()
        #
    
    def capture(self):
        subject = "capture"
        body = "capture please"

        # self.sender.send_mail(["nguyenhieu82132@gmail.com"], subject, body)

    def show(self):
        # Show len cai email
        print()

