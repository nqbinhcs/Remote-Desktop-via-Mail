import os

class Application:
    def __init__(self):
        pass

    def run(self, code, id=0):
        if code == 'view':
            return self.view()
        elif code == 'kill':
            return self.kill(id)
 
    def view(self):
        return os.popen('powershell "gps | where {$_.MainWindowTitle } | select name, id, {$_.Threads.Count}').read()
    
    def kill(self, id):
        try:
            os.kill(id, 9)
        except OSError:
            return False
        return True