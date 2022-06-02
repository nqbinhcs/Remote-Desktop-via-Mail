import os
import shutil
from sys import gettrace

class FileSystem:

    '''
    Return 2d array :
        [<File Number>, <File Name>]
        Ex:
            [1, "Github"]
                [2, "Remote-Desktop-Via-Mail]
                [2, "Contacts-App]
                    [3, "data"]
                    ....
                     
    '''

    def __init__(self):
        # get all
        self.path = ''

        self.getPath()

        self.components = self.split(self.path)

        # self.show()

    def run(self, code):
        if code == 'view':
            return self.getTree()
        elif code == 'copy':
            return self.copy(r"C:/Users/nguye/Downloads/PHONGTHI_HK2_2122_LINH TRUNG_NVC.xls", r"C:/Users/nguye/Desktop/PHONGTHI_HK2_2122_LINH TRUNG_NVC.xls")
        elif code == 'download':
            return self.download()
        else:
            return 'wrong code'

    def split(self, path):
        return path.split('\\')

    def getPath(self):
        self.path = os.getcwd()
        # return self.system

    def getTree(self):
        tree = []

        path = ''
        for i in self.components[:-2]:
            path += i + '\\'

        path = path[:-1]


        for root, dirs, files in os.walk(path):
        # for root, dirs, files in os.walk(self.components[0]+'\\'):
            component = self.split(root)
            stt = len(component)-1
            tree.append([stt, component[-1]])
            for file in files:
                tree.append([stt+1, file])

        # self.show(tree)
        return tree

    def show(self, tree):
        symbols = ['-', '+', '*', '~', '@', '#', '$']
        l = len(symbols)
        start = tree[0][0]
        for dir in tree:
            for i in range(dir[0]-start):
                print('  ', end='')
            print(symbols[(dir[0]-start) % l] + ' ' + dir[1])

    def copy(self, src_path, dst_path):
        shutil.copyfile(src_path, dst_path)
        return True

    def download(self):
        print('download - <just attach the file>')

FileSystem()
