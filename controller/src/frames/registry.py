from textwrap import fill
from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ANCHOR, PhotoImage

import src.sender as sender
import src.textstyles as style
import src.themecolors as themecolor

class Registry(tk.Frame, sender.Sender):
    def __init__(self, parent, sender):
        tk.Frame.__init__(
            self, parent, bg=themecolor.background)
        
        self.sender = sender

        self.logo = tk.Label(self, text="Registry")
        self.logo.pack()

        self.emchiu = tk.Label(self, text="Em chiu cai nay, khong hieu registry la lam gi")
        self.emchiu.pack(pady=(20, 0))

        self.btn_frame = tk.Frame(self, bg=themecolor.background) 
        self.btn_frame.pack(side=tk.LEFT)
        
        self.show_frame = tk.Frame(self, bg=themecolor.background)                                        # width=width*2.0/3.0)
        self.show_frame.pack(side=tk.RIGHT)

        self.create_widgets()
    
    def create_widgets(self):
        print()
   