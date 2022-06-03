import os
import shutil
from sys import gettrace

class FileSystem:
    def __init__(self):
        pass
 
    def run(self, code, src_path = r"", dst_folder=r""):
        if code == 'view':
            return self.getTree()
        elif code == 'copy':
            return self.copy(src_path, dst_folder)
        elif code == 'download':
            return self.download()
        
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

    def copy(self, src_path, dst_folder):
        try:
            dst_path = os.path.join(dst_folder, src_path.split('\\')[-1])
            print(dst_path)
            shutil.copyfile(src_path, dst_path)
        except OSError:
            return False
        return True

    def download(self):
        print('attach file')