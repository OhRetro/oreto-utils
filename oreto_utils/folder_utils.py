#Folder

from os.path import isdir as osp_isdir, getsize as osp_getsize, join as osp_join
from os import mkdir as os_mkdir, listdir as os_listdir, remove as os_remove, walk as os_walk, rename as os_rename
from shutil import rmtree as sh_rmtree, move as sh_move, copytree as sh_copytree
from tkinter import Tk, filedialog

class Folder:
    def __init__(self, folder_name, parent_folder="./"):
        self.folder_name = folder_name
        self.parent_folder = parent_folder
        self.attrs = {}
        self.update()        

    #It will update the parent folder and folder name
    def update(self):
        #Check if the parent folder have "\" to replace with "/"
        if "\\" in self.parent_folder:
            self.parent_folder = self.parent_folder.replace("\\", "/")

        #Check if the folder path ends with "/"
        if not self.parent_folder.endswith("/"):
            self.parent_folder = f"{self.parent_folder}/"
        
        self.folder = self.parent_folder+self.folder_name

        self.attrs["NAME"] = self.folder_name
        self.attrs["PARENT"] = self.parent_folder
        self.attrs["FOLDER"] = self.folder
        
    def getattr(self, attr_name:str="ALL"):
        return self.attrs if attr_name in {"ALL", ""} else self.attrs[attr_name]

    #It will rename the folder name
    def rename(self, new_folder_name):
        old_folder = self.folder
        self.folder_name = new_folder_name
        self.update()
        os_rename(old_folder, self.folder)

    #It will return True if the folder exists
    def exists(self):
        return osp_isdir(f"{self.folder}")
    
    #It will create the folder
    def create(self):
        if self.exists():
            raise FileExistsError
        
        os_mkdir(f"{self.folder}")
        
    #It will delete the folder
    def delete(self):
        if not self.exists():
            raise FileNotFoundError
        
        sh_rmtree(f"{self.folder}")

    #It will delete all the contents of the folder and will check if a folder or a file
    def deletecontents(self, exception:list=None):
        if not self.exists():
            raise FileNotFoundError

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            if osp_isdir(f"{self.folder}/{content}"):
                sh_rmtree(f"{self.folder}/{content}")
            else:
                os_remove(f"{self.folder}/{content}")
                                
    #It will move the folder
    def move(self, path_destiny:str):
        if not self.exists():
            raise FileNotFoundError

        old_parent = self.parent_folder
        self.parent_folder = path_destiny
        self.update()

        sh_move(old_parent, path_destiny)
    
    #It will move the contents of the folder into another folder
    def movecontents(self, destiny:str, exception:list=None):
        if not self.exists():
            raise FileNotFoundError

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            sh_move(f"{self.folder}/{content}", f"{destiny}/{content}")

    #It will copy the folder to the destiny
    def copy(self, path_destiny:str):
        if not self.exists():
            raise FileNotFoundError

        if not osp_isdir(path_destiny):
            raise NotADirectoryError

        sh_copytree(self.folder, path_destiny)
        
    #It will copy the contents of the folder to the destiny
    def copycontents(self, path_destiny:str, exception:list=None):
        if not self.exists():
            raise FileNotFoundError

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            sh_copytree(f"{self.folder}/{content}", f"{path_destiny}/{content}")      
    #It will list all the contents of the folder
    def list(self):
        if not self.exists():
            raise FileNotFoundError

        return os_listdir(f"{self.folder}")
        
    #It will count all the contents inside the folder
    def count(self):
        if not self.exists():
            raise FileNotFoundError

        return sum(1 for _ in self.list())
    
    #A dialog to select a folder will appear after that it will setup and separate the parent folder and folder name 
    def select(self):
        root = Tk()
        root.withdraw()
        selected_folder = filedialog.askdirectory()
        
        if selected_folder == "":
            return None
      
        self.folder_name = selected_folder.split("/")[-1]
        self.parent_folder = "/".join(selected_folder.split("/")[:-1])+"/"
        self.update()
        root.destroy()
        return True
        
    #It will get the folder total size and return it in bytes
    def size(self):
        if not self.exists():
            raise FileNotFoundError

        size = 0
        for path, dirs, files in os_walk(self.folder):
            for f in files:
                fp = osp_join(path, f)
                size += osp_getsize(fp)
                
        return size