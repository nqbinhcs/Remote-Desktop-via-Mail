from decimal import MAX_EMAX
from multiprocessing.dummy import Process
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Progressbar


def messagebox(title="client", msg="Done", type="info"):
    # type are: warn, error, info
    title = title.capitalize()
    if type == "error":
        tk.messagebox.showerror(title, msg)
    elif type == "warn":
        tk.messagebox.showwarning(title, msg)
    else:
        tk.messagebox.showinfo(title, msg)


class inputbox(tk.Frame):
    # Mainly used for killing and starting application or process
    def __init__(self, master, tl="?", cmd="?"):
        super().__init__(master)
        tl = tl.capitalize()
        cmd = cmd.capitalize()
        self.master = master
        self.master.title(tl + " " + cmd)
        self.master.resizable(False, False)

        self.input_field = tk.Entry(
            self.master, textvariable="Nhập ID", width=30)
        self.input_field.focus()
        self.input_field.pack(side=tk.LEFT, padx=20, pady=20)

        self.btn_get = tk.Button(self.master, text=cmd, width=15)
        self.btn_get.pack(side=tk.LEFT, padx=20, pady=20)

    def getvalue(self):
        return self.input_field.get()

    def clear(self):
        self.input_field.delete(0, tk.END)

    def killbox(self):
        self.master.destroy()


class ProgressBar():
    def __init__(self):
        self.loading_screen = tk.Tk()
        self.loading_screen.title('loading...')
        self.pgb_load = Progressbar(
            self.loading_screen, orient=HORIZONTAL, length=300, mode='determinate')
        # self.pgb_load.pack(side=tk.TOP, padx=20, pady=20)
        self.pgb_load.pack()

    def update(self, length):
        self.pgb_load['value'] = length

    def concat(self, length):
        self.pgb_load['value'] += length

    def step(self):
        if self.pgb_load['value'] == 300:
            self.pgb_load['value'] = 0
        else:
            self.pgb_load['value'] += 60

    def killbox(self):
        self.master.destroy()

