import os


class Process():
    def __init__(self):
        pass

    def run(self, code, id=0):
        if code == 'view':
            return self.process_view()
        elif code == 'kill':
            return self.process_kill(id)
        return False

    def process_view(self):
        try:
            data = os.popen(
                'powershell "gps |  select name, id, {$_.Threads.Count}').read()
            return data
        except OSError:
            return False

    def process_kill(self, process_ID):
        try:
            os.kill(process_ID, 9)
        except OSError:
            return False
        return True
