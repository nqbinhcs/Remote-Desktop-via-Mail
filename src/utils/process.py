import os


class Process():
    """An class for managing processes
    """

    def run(self, code, id=0):
        """View processes or kill a specific process

        :param code: (str) 'view' or 'kill'
        :param id: (int) ID of the process, defaults to 0
        :return: (str) result after executing command
        """
        if code == 'view':
            return self.process_view()
        elif code == 'kill':
            return self.process_kill(id)
        return False

    def process_view(self):
        """View all processes

        :return: (str) all processes
        """
        try:
            data = os.popen(
                'powershell "gps |  select name, id, {$_.Threads.Count}').read()
            return data
        except OSError:
            return False

    def process_kill(self, process_ID):
        """Kill an application

        :param process_ID: (int) ID of the process
        :return: (bool) status of command
        """
        try:
            os.kill(process_ID, 9)
        except OSError:
            return False
        return True
