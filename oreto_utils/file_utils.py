#File(s)

from os import remove as os_remove, rename as os_rename
from os.path import isfile as osp_isfile, getsize as osp_getsize, isdir as osp_isdir, abspath as osp_abspath
from shutil import move as sh_move, copy as sh_copy
from tkinter import Tk, filedialog

class File:
    def __init__(self, file_name, file_ext, file_path="./"):
        self.file_name = file_name
        self.file_path = file_path
        self.file_ext = file_ext
        self.attrs = {}
        self.update()
        
    #It will update the file path, file name and file extension
    def update(self):
        #Check if the file path have "\" to replace with "/"        
        if "\\" in self.file_path:
            self.file_path = self.file_path.replace("\\", "/")
        
        #Check if the file path ends with "/"
        if not self.file_path.endswith("/"):
            self.file_path = f"{self.file_path}/"

        #Check if the file extension starts with "."
        if not self.file_ext.startswith(".") and self.file_ext != "":
            self.file_ext = f".{self.file_ext}"

        self.file = self.file_path+self.file_name+self.file_ext
        self.file_full_path = osp_abspath(self.file).replace("\\", "/")
        
        self.attrs["NAME"] = self.file_name
        self.attrs["EXT"] = self.file_ext
        self.attrs["FILE"] = self.file
        self.attrs["FILE_EXT"] = self.file_name+self.file_ext
        self.attrs["PATH"] = self.file_path
        self.attrs["FULL_PATH"] = self.file_full_path
        
    def getattr(self, attr_name:str="ALL"):
        return self.attrs if attr_name in {"ALL", ""} else self.attrs[attr_name]
        
    #It will rename the file name
    def rename(self, new_file_name):
        old_file = self.file
        self.file_name = new_file_name
        self.update()
        os_rename(old_file, self.file)
        
    #It will return the file content
    def read(self):
        if not self.exists():
            raise FileNotFoundError("There is no such file to read.")
        
        with open(f"{self.file}", "r") as f:
            f_content = f.read()
            f.close()
            return f_content
                    
    #It will write the content in the file
    def write(self, file_content=""):
        with open(f"{self.file}", "w") as f:
            f.write(file_content)
            f.close()
                    
    #It will delete the file
    def delete(self):
        if not self.exists():
            raise FileNotFoundError("There is no such file to delete.")

        os_remove(f"{self.file}")

    #It will move the file to the destiny path
    def move(self, path_destiny:str):
        if not self.exists():
            raise FileNotFoundError("There is no such file to move.")

        old_path = self.file
        self.file_path = path_destiny
        self.update()

        sh_move(old_path, path_destiny)
        
    #It will copy the file to the destiny path
    def copy(self, path_destiny:str):
        if not self.exists():
            raise FileNotFoundError("There is no such file to copy.")

        if not osp_isdir(path_destiny):
            raise NotADirectoryError("There is no such directory to copy the file into.")
        
        sh_copy(self.file, path_destiny)
        
    #It will return True if the file exists
    def exists(self):
        return osp_isfile(f"{self.file}")
    
    #A dialog to select a file will appear after that it will setup and separate the file path, the file name and file extension 
    def select(self, title:str="Select a file", initialdir:str=None, filetypes:list=None):
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
        root = Tk()
        root.withdraw()
        selected_file = filedialog.askopenfilename(title=title, initialdir=initialdir, filetypes=filetypes)

        if selected_file == "":
            return False, None

        self.file_name = selected_file.split("/")[-1].split(".")[0]
        self.file_ext = selected_file.split("/")[-1].split(".")[-1]
        self.file_path = "/".join(selected_file.split("/")[:-1])+"/"
        self.update()
        root.destroy()
        return True
            
    #It will get the file total size return it in bytes
    def size(self):
        if not self.exists():
            raise FileNotFoundError("There is no such file to get the size.")

        return osp_getsize(self.file)
    
class Files:
    def select(self, title:str="Select a file", initialdir:str=None, filetypes:list=None, multiple:bool=True):
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
        root = Tk()
        root.withdraw()
        selected_file = filedialog.askopenfilename(title=title, initialdir=initialdir, filetypes=filetypes, multiple=multiple)

        if selected_file == "":
            return False
        
        root.destroy()
        return selected_file