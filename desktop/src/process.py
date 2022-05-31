# from src.sender import Sender
import os

class Process():
    def __init__(self):
        pass

    def run(self, code):
        if code == 'view':
            return self.process_view()
        elif code == 'kill':
            return self.process_kill()
        else:
            return "<send error message: Code incorrect>"

    def process_view(self):
        return  os.popen('powershell "gps |  select name, id, {$_.Threads.Count}').read()

    def process_kill(self):
        return "kill"
