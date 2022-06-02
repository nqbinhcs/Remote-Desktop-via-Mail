import os


class Application:
    def __init__(self):
        pass

    def run(self, code):
        if code == 'view':
            return self.view()
        elif code == 'kill':
            return self.kill(26944)

    def view(self):
        return os.popen('powershell "gps | where {$_.MainWindowTitle } | select name, id, {$_.Threads.Count}').read()

    def kill(self, id):
        print('before:')
        print(self.view())
        os.kill(id, 9)
        print('after:')
        print(self.view())
        return True
