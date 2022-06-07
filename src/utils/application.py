import os


class Application:
    """An class for managing applications
    """

    def run(self, code, id=0):
        """View applications or kill a specific application
        :param code: (str) 'view' or 'kill'
        :param id: (int) ID of the application, defaults to 0
        :return: (str) result after executing command
        """
        if code == 'view':
            return self.view()
        elif code == 'kill':
            return self.kill(id)

    def view(self):
        """View all applications
        :return: (str) all applications
        """
        return os.popen('powershell "gps | where {$_.MainWindowTitle } | select name, id, {$_.Threads.Count}').read()

    def kill(self, id):
        """Kill an application
        :param id: (int) ID of the application
        :return: (bool) status of command
        """
        try:
            os.kill(id, 9)
        except OSError:
            return False
        return True
