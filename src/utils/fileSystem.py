from http.client import PARTIAL_CONTENT
from multiprocessing import parent_process
import os
import shutil
from pathlib import Path

class FileSystem:
    def __init__(self):
        pass
 
    def run(self, code, parameters):
        if code == 'view':
            return self.getTree()
        elif code == 'copy':
            return self.copy(parameters)
        elif code == 'download':
            return self.download(parameters)
        
        return False

    def getTree(self):
        self.components = os.getcwd().split('\\')
        
        tree = []

        for root, _, files in os.walk(self.components[0]+'\\'):
            component = root.split('\\')
            stt = len(component)-1
            tree.append([stt, component[-1]])
            for file in files:
                tree.append([stt+1, file])

        return tree

    def copy(self, parameters):
        _, src, _, dst, _ = parameters.split('"')
        src = src.replace("/","\\")
        dst = dst.replace("/","\\")


        try:
            dst_path = os.path.join(dst, src.split('\\')[-1])
            shutil.copyfile(src, dst_path)
        except OSError:
            return False
        return True

    def download(self, parameters):
        print('attach file')