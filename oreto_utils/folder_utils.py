#Folder(s)

from os.path import isdir as osp_isdir, getsize as osp_getsize, join as osp_join, isfile as osp_isfile
from os import mkdir as os_mkdir, listdir as os_listdir, remove as os_remove, walk as os_walk, rename as os_rename
from shutil import rmtree as sh_rmtree, move as sh_move, copytree as sh_copytree, copyfile as sh_copyfile
from tkinter import Tk, filedialog

__all__ = ["Folder", "Folders"]

class Folder:
    def __init__(self, folder_name, parent_folder="./"):
        self.folder_name = folder_name
        self.parent_folder = parent_folder
        self.attrs = {}
        self._update()        

    #It will update the parent folder and folder name
    def _update(self) -> None:
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
        
    def getattr(self, attr_name:str="ALL") -> dict:
        return self.attrs if attr_name in {"ALL", ""} else self.attrs[attr_name]

    #It will rename the folder name
    def rename(self, new_folder_name) -> None:
        old_folder = self.folder
        self.folder_name = new_folder_name
        self._update()
        os_rename(old_folder, self.folder)

    #It will return True if the folder exists
    def exists(self) -> bool:
        return osp_isdir(f"{self.folder}")
    
    #It will create the folder
    def create(self) -> None:
        if self.exists():
            raise FileExistsError("The folder already exists")
        
        os_mkdir(f"{self.folder}")
        
    #It will delete the folder
    def delete(self) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to delete.")
        
        sh_rmtree(f"{self.folder}")

    #It will delete all the contents of the folder and will check if a folder or a file
    def deletecontents(self, exception:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to delete the contents.")

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            if osp_isdir(f"{self.folder}/{content}"):
                sh_rmtree(f"{self.folder}/{content}")
            elif osp_isfile(f"{self.folder}/{content}"):
                os_remove(f"{self.folder}/{content}")
                                
    #It will move the folder
    def move(self, path_destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to move.")

        old_parent = self.parent_folder
        self.parent_folder = path_destiny
        self._update()

        sh_move(old_parent, path_destiny)
    
    #It will move the contents of the folder into another folder
    def movecontents(self, destiny:str, exception:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to move the contents.")

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            sh_move(f"{self.folder}/{content}", f"{destiny}/{content}")
            
    #It will copy the folder to the destiny
    def copy(self, path_destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to copy.")

        if not osp_isdir(path_destiny):
            raise NotADirectoryError("The destiny is not a folder.")

        sh_copytree(self.folder, path_destiny)
        
    #It will copy the contents of the folder to the destiny and will check if a folder or a file
    def copycontents(self, path_destiny:str, exception:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to copy the contents.")

        if exception is None:
            exception = []

        contents = self.list()
        
        for ex in exception:
            if ex in contents:
                contents.remove(ex)

        for content in contents:
            if osp_isdir(f"{self.folder}/{content}"):
                sh_copytree(f"{self.folder}/{content}", f"{path_destiny}/{content}")
            elif osp_isfile(f"{self.folder}/{content}"):
                sh_copyfile(f"{self.folder}/{content}", f"{path_destiny}/{content}")
                  
    #It will list all the contents of the folder
    def list(self) -> list:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to list the contents.")

        return os_listdir(f"{self.folder}")
        
    #It will count all the contents inside the folder
    def count(self) -> int:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to count the contents.")

        return sum(1 for _ in self.list())
    
    #A dialog to select a folder will appear after that it will setup and separate the parent folder and folder name 
    def select(self, title:str="Select a folder", initialdir:str=None, mustexist:bool=False) -> bool:
        """It can return a boolean value to indicate if the folder was selected or not."""
        root = Tk()
        root.withdraw()
        selected_folder = filedialog.askdirectory(title=title, initialdir=initialdir, mustexist=mustexist)
        root.destroy()
        
        if selected_folder != "":      
            self.folder_name = selected_folder.split("/")[-1]
            self.parent_folder = "/".join(selected_folder.split("/")[:-1])+"/"
            self._update()
            return True
        else:
            return False
        
    #It will get the folder total size and return it in bytes
    def size(self) -> int:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to get the size.")

        size = 0
        for path, dirs, files in os_walk(self.folder):
            for f in files:
                fp = osp_join(path, f)
                size += osp_getsize(fp)
                
        return size
    
class Folders:
    def select(title:str="Select a folder", initialdir:str=None, mustexist:bool=True) -> str:
        root = Tk()
        root.withdraw()
        selected_folder = filedialog.askdirectory(title=title, initialdir=initialdir, mustexist=mustexist)      
        root.destroy()
        return selected_folder