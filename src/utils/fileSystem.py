from http.client import PARTIAL_CONTENT
from multiprocessing import parent_process
import os
import shutil
from pathlib import Path


class FileSystem:
    """An class for managing files
    """

    def run(self, code, parameters):
        """View, copy and download files

        :param code: (str) 'view', 'copy', or 'download'
        :param parameters: (str) directory
        :return: (str) result after executing command
        """
        if code == 'view':
            return self.getTree()
        elif code == 'copy':
            return self.copy(parameters)
        elif code == 'download':
            return self.download(parameters)

        return False

    def getTree(self, path=None):
        """Get files in directory
        :param path: (str) 
        :return: (list) list of files
        """
        if path == None:
            path = os.getcwd().split('\\')[0]
        else:
            path = path[:-2]
        tree = os.listdir(path+'\\')
        tree.append(path)

        i = 0
        j = len(tree) - 2
        while i < len(tree) - 1:
            if os.path.isfile(os.path.join(path, tree[i])):
                tmp = tree[i]
                tree[i] = tree[j]
                tree[j] = tmp
                j -= 1
                i -= 1
            i += 1
            if i == j:
                break

        return tree

    def copy(self, parameters):
        """Copy a file from source to destination

        :param parameters: (str) 
        :return: (bool) status after copying
        """
        _, src, _, dst, _ = parameters.split('"')
        src = src.replace("/", "\\")
        dst = dst.replace("/", "\\")

        try:
            dst_path = os.path.join(dst, src.split('\\')[-1])
            shutil.copyfile(src, dst_path)
        except OSError:
            return False
        return True

    def download(self, parameters):
        """Download a file with path provided
        :param parameters: (str)
        :return: (str) file
        """
        return parameters
