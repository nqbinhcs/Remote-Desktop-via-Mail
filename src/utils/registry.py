import winreg
import os

# FORMAT ! 
'''
Email:

Subject: RDM-REGISTRY
Content:
    <["wirte", "get", "create", "set", "delete-value", "delete-key"]>
    <parameters>
'''
 
# Type
'''
1. Write registry file
    Two types:
        1) text: be written on the content block of the email
            Creating a .reg file - fileReg.reg, to store the text from the content block (in .temp folder)
            #--> The content block is NOT EMPTY!

        2) fileReg.reg: be attached to the email 
            The file - fileReg.reg, will be downloaded and saved in .temp folder
            #--> The content block is EMPTY!

# Parameters:
        + Path: <HKEY>/.../<Name of a program>
        + Name: name of a registry
        + Value: value of a registry
        + Datatype: [String, Binary, DWORD, QWORD, Multi-String, Expandable string]


2. Get value of registry

    Content: <Path>,<Name>


3. Create a new registry

    Content: <Path>,<Name>


4. Set registry: set value of a particular registry

    Content: <Path>,<Name>,<Datatype>,<Value>


5. Delete value of a registry

    Content: <Path>,<Name>


6. Delete a key

    Content: <Path>

'''

class Registry:
    def __init__(self):
        pass

    def run(self, code, parameters=None):
        if code == 'write':
            return self.write_file_registry(parameters)

        HKEY, Pars = parameters.split(',', 1)
        # Pars storing parameters, such as: path, name, value, datatype (maybe)
        Pars = Pars.split(',')

        HKEY = self.baseRegistryKey(HKEY)
        if not HKEY:
            return False
        
        reg = winreg.ConnectRegistry(None, HKEY)

        if (code == "get") & (len(Pars) == 2):
            return self.get_registry(reg, Pars[0], Pars[1])
        elif (code == "create") & (len(Pars) == 1):
            return self.create_registry(reg, Pars[0])
        elif (code == "set") & (len(Pars) == 4):
            return self.set_registry(reg, Pars[0], Pars[1], Pars[2], Pars[3])
        elif (code == "delete-value") & (len(Pars) == 2):
            return self.delete_value_registry(reg, Pars[0], Pars[1])
        elif (code == "delete-key") & (len(Pars) == 1):
            return self.delete_key_registry(reg, Pars[0])
        
        return False


    # type 1
    def write_file_registry(self, parameters=None):
        if parameters:
            # Case 1: Create fileReg.reg in .temp folder
            fi = open(os.path.join(".temp", "fileReg.reg"), "wb")
            fi.write(parameters)
            fi.close()

        try:
            os.popen("regedit.exe /s fileReg.reg")
        except OSError:
            os.remove(os.path.join(".temp", "fileReg.reg"))
            return False

        return True


    # type 2
    def get_registry(self, reg, path, name):

        try:
            key =  winreg.OpenKey(reg, path, 0, winreg.KEY_QUERY_VALUE)
            result = winreg.QueryValueEx(key, name) 
            
            if not result[0]:
                return False
            else:
                if (result[1] == winreg.REG_MULTI_SZ):
                    data = ''
                    for x in result[0]: data += x + '\n'
                elif (result[1] == winreg.REG_BINARY):
                    data = ' '.join('%02x' % x for x in result[0])
                else:
                    data = str(result[0])
            winreg.CloseKey(key) 

            return data

        except OSError:
            return False


    # type 3
    def create_registry(self, reg, path):
        try:
            winreg.CreateKey(reg, path)
        except OSError:
            return False
        
        return True


    # type 4
    def set_registry(self, reg, path, name, datatype, value):

        datatype = self.baseDataType(datatype)

        try:
            if datatype in [winreg.REG_DWORD, winreg.REG_QWORD]:
                value = int(value)
            elif datatype == winreg.REG_MULTI_SZ:
                value = value.split('\n')
            elif datatype == winreg.REG_BINARY:
                value = value.replace(' ', '')
                value = bytearray.fromhex(value)
            key =  winreg.OpenKey(reg, path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, name, 0, datatype, value)
            winreg.CloseKey(key)
            
        except OSError:
            return False

        return True


    # type 5
    def delete_value_registry(self, reg, path, name):
        try:
            key =  winreg.OpenKey(reg, path, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, name)

        except OSError:
            return False

        return True


    # type 6
    def delete_key_registry(self, reg, path):
        try:
            winreg.DeleteKeyEx(reg, path)

        except OSError:
            return False

        return True
        

    def baseRegistryKey(self, name):
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