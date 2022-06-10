import winreg
import os


class Registry:
    """A class for managing registry
    """

    def __init__(self):
        pass

    def run(self, code, parameters=None):
        """Write a new key / Get value / Create an empty key / Set value of a key / Delete value of a key /Delete key

        :param code: (str) 'write' / 'get' / 'create' / 'set' / 'delete-value' / 'delete-key'
        :param parameters: (str) path of a key or value of key,...
        :return: value if the code is 'get', else True if the process is successful and False if not
        """
        if code == 'write':
            return self.write_file_registry(parameters)

        # parameters += ','
        HKEY, Pars = parameters.split(',', 1)
        # Pars storing parameters, such as: path, name, value, datatype (maybe)
        Pars = Pars.split(',')

        print(HKEY)
        print('Pars: ')
        print(Pars)

        HKEY = self.baseRegistryKey(HKEY)
        if not HKEY:
            return False

        reg = winreg.ConnectRegistry(None, HKEY)

        if (code == "get") & (len(Pars) == 2):
            return self.get_registry(reg, Pars[0], Pars[1])
        elif (code == "create") & (len(Pars) == 2):
            return self.create_registry(reg, Pars[0], Pars[1])
        elif (code == "set") & (len(Pars) == 4):
            return self.set_registry(reg, Pars[0], Pars[1], Pars[2], Pars[3])
        elif (code == "delete-value") & (len(Pars) == 2):
            return self.delete_value_registry(reg, Pars[0], Pars[1])
        elif (code == "delete-key") & (len(Pars) == 1):
            return self.delete_key_registry(reg, Pars[0])

        return False

    # type 1

    def write_file_registry(self, parameters=None):
        """Write a new value on the system

        :param parameters: (str) None if user sent a file .reg or some block of code according file .reg structure 
        :return: (bool) True if the process is successful and False if not
        """
        if parameters:
            # Case 1: Create fileReg.reg in .temp folder
            fi = open(os.path.join(".temp", "fileReg.reg"), "w")
            fi.write(parameters)
            fi.close()

        try:
            cmd = os.path.join(os.getcwd(), ".temp", "fileReg.reg")
            os.popen("regedit.exe /s " + cmd)
        except OSError:
            os.remove(os.path.join(".temp", "fileReg.reg"))
            return False

        return True

    # type 2

    def get_registry(self, reg, path, name):
        """Get the value of a key according path and name

        :param reg: (register hotkey) includes: classes root, current user, local machine, users, current cofig
        :param path: (str) leads to the key
        :param name: (str) name of the value which user want to get
        :return: (bool) True if the process is successful and False if not 
        """
        try:
            path = path.replace('/', '\\')
            key = winreg.OpenKey(reg, path, 0, access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            result = winreg.QueryValueEx(key, name)

            if not result[0]:
                return False
            else:
                if (result[1] == winreg.REG_MULTI_SZ):
                    data = ''
                    for x in result[0]:
                        data += x + '\n'
                elif (result[1] == winreg.REG_BINARY):
                    data = ' '.join('%02x' % x for x in result[0])
                else:
                    data = str(result[0])
            winreg.CloseKey(key)

            return data

        except OSError:
            return False

    # type 3

    def create_registry(self, reg, path, key_name):
        """Create an empty key (without value) according the path

        :param reg: (registry hotkey) includes: classes root, current user, local machine, users, current cofig
        :param path: (str) leads to the key
        :return: (bool) True if the process is successful and False if not
        """
        try:
            path += '/' + key_name
            path = path.replace('/', '\\')
            winreg.CreateKey(reg, path)
        except OSError:
            return False

        return True

    # type 4

    def set_registry(self, reg, path, name, datatype, value):
        """Set value of a key according path & name

        :param reg: (register hotkey) includes: classes root, current user, local machine, users, current cofig
        :param path: (str) leads to the key
        :param name: (str) name of the value which user want to set
        :param datatype: (registry datatype) includes: binary (Binary data), dword (Numeral), qwrod (64-bit numeric value), text (sz), mutul sz (array of strings) 
        :param value: (str) new value
        :return: (bool) True if the process is successful and False if not
        """

        datatype = self.baseDataType(datatype)

        try:
            if datatype in [winreg.REG_DWORD, winreg.REG_QWORD]:
                value = int(value)
            elif datatype == winreg.REG_MULTI_SZ:
                value = value.split('\n')
            elif datatype == winreg.REG_BINARY:
                value = value.replace(' ', '')
                value = bytearray.fromhex(value)
            path = path.replace('/', '\\')
            key = winreg.OpenKey(reg, path, 0, access=winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, name, 0, datatype, value)
            winreg.CloseKey(key)

        except OSError:
            return False

        return True

    # type 5

    def delete_value_registry(self, reg, path, name):
        """Delete value of a registry according path & name

        :param reg: (register hotkey) includes: classes root, current user, local machine, users, current cofig
        :param path: (str) leads to the key
        :param name: (str) name of the value which user want to delete
        :return: (bool) True if the process is successful and False if not
        """
        try:
            path = path.replace('/', '\\')
            key = winreg.OpenKey(reg, path, 0, access=winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, name)

        except OSError:
            return False

        return True

    # type 6

    def delete_key_registry(self, reg, path):
        """Delete a registry according path

        :param reg: (register hotkey) includes: classes root, current user, local machine, users, current cofig
        :param path: (str) leads to the key
        :return: (bool) True if the process is successful and False if not
        """
        return self.deleteSubkey(reg, path)

    def deleteSubkey(self, reg, key1, key2=""):
        """Delete all of key1's subkeys and then delete key1 key 

        :param reg: (register hotkey) includes: classes root, current user, local machine, users, current cofig
        :param key1: (str) leads to key1 key
        :param key2: (str) name of subkey of key1 key
        :return: (bool) True if the process is successful and False if not
        """
        if key2 == "":
            currentkey = key1
        else:
            currentkey = key1 + "\\" + key2

        try:
            open_key = winreg.OpenKey(
                reg, currentkey, 0, access=winreg.KEY_ALL_ACCESS)
            infokey = winreg.QueryInfoKey(open_key)
            for x in range(0, infokey[0]):
                subkey = winreg.EnumKey(open_key, 0)
                try:
                    winreg.DeleteKey(open_key, subkey)
                except:
                    self.deleteSubkey(reg, currentkey, subkey)

            winreg.DeleteKey(open_key, "")
            open_key.Close()
        except:
            return False
        return True

    def baseRegistryKey(self, name):
        """Get register hotkey according name

        :param name: (str) "HKEY_CLASSES_ROOT" / "HKEY_CURRENT_USER" / "HKEY_LOCAL_MACHINE" / "HKEY_USERS" / "HKEY_CURRENT_CONFIG"
        :return: (registry hotkey) corresponding to name
        """
        if (len(name) == 0):
            return None
        if name == "HKEY_CLASSES_ROOT":
            return winreg.HKEY_CLASSES_ROOT
        elif name == "HKEY_CURRENT_USER":
            return winreg.HKEY_CURRENT_USER
        elif name == "HKEY_LOCAL_MACHINE":
            return winreg.HKEY_LOCAL_MACHINE
        elif name == "HKEY_USERS":
            return winreg.HKEY_USERS
        elif name == "HKEY_CURRENT_CONFIG":
            return winreg.HKEY_CURRENT_CONFIG
        else:
            return None

    def baseDataType(self, name):
        """Get datatype according name

        :param name: (str) "String" / "Binary" / "DWORD" / "QWORD" / "Multi-String" / "Expandable string"
        :return: (registry hotkey) corresponding to name
        """
        if len(name) == 0:
            return None
        if name == "String":
            return winreg.REG_SZ
        elif name == "Binary":
            return winreg.REG_BINARY
        elif name == "DWORD":
            return winreg.REG_DWORD
        elif name == "QWORD":
            return winreg.REG_QWORD
        elif name == "Multi-String":
            return winreg.REG_MULTI_SZ
        elif name == "Expandable string":
            return winreg.REG_EXPAND_SZ
        else:
            return None
