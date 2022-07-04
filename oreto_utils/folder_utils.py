#Folder(s)

from os.path import isdir as osp_isdir, getsize as osp_getsize, join as osp_join, isfile as osp_isfile, abspath as osp_abspath
from os import mkdir as os_mkdir, listdir as os_listdir, remove as os_remove, walk as os_walk, rename as os_rename
from shutil import rmtree as sh_rmtree, move as sh_move, copytree as sh_copytree, copyfile as sh_copyfile
from oreto_utils.tkinter_utils import dialog as outk_dialog
from oreto_utils.others_utils import formatsize as ouo_formatsize

__all__ = ["Folder", "folderselect", "foldersize", "folderlist"]

class Folder:
    def __init__(self, folder, parent="./"):
        self._folder = {
            "FOLDER": folder,
            "PARENT": parent,
            "PATH": None,
            "FULL_PATH": None
        }
        self._update()        

    #It will update the parent folder and folder name
    def _update(self) -> None:
        #Check if the parent folder have "\" to replace with "/"
        if "\\" in self._folder["PARENT"]:
            self._folder["PARENT"] = self._folder["PARENT"].replace("\\", "/")

        #Check if the folder path ends with "/"
        if not self._folder["PARENT"].endswith("/"):
            self._folder["PARENT"] = f"{self._folder['PARENT']}/"
        
        self._folder["PATH"] = self._folder["PARENT"]+self._folder["FOLDER"]
        self._folder["FULL_PATH"] = osp_abspath(self._folder["PATH"]).replace("\\", "/")

    #It will rename the folder name
    def rename(self, newname) -> None:
        old_folder = self._folder["FULL_PATH"]
        self._folder["FOLDER"] = newname
        self._update()
        os_rename(old_folder, self._folder["FULL_PATH"])
    
    #It will create the folder
    def create(self) -> None:
        if self.exists():
            raise FileExistsError("The folder already exists")
        
        os_mkdir(f"{self._folder['FULL_PATH']}")
        
    #It will delete the folder
    def delete(self) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to delete.")
        
        sh_rmtree(f"{self._folder['FULL_PATH']}")

    #It will move the folder
    def move(self, destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to move.")

        old_parent = self._folder["PARENT"]
        self._folder["PARENT"] = destiny
        self._update()

        sh_move(old_parent, destiny)
    
    #It will copy the folder to the destiny
    def copy(self, destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to copy.")

        if not osp_isdir(destiny):
            raise NotADirectoryError("The destiny is not a folder.")

        sh_copytree(self._folder["FULL_PATH"], destiny)
        
    #It will delete all the contents of the folder
    def deletecontents(self, exceptions:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to delete the contents.")

        contents = self.list()
        
        if exceptions:            
            for exception in exceptions:
                if exception in contents:
                    contents.remove(exception)

        for content in contents:
            if osp_isdir(f"{self._folder['FULL_PATH']}/{content}"):
                sh_rmtree(f"{self._folder['FULL_PATH']}/{content}")
            elif osp_isfile(f"{self._folder['FULL_PATH']}/{content}"):
                os_remove(f"{self._folder['FULL_PATH']}/{content}")
                                
    #It will move the contents of the folder into another folder
    def movecontents(self, destiny:str, exceptions:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to move the contents.")

        contents = self.list()
        
        if exceptions:        
            for exception in exceptions:
                if exception in contents:
                    contents.remove(exception)

        for content in contents:
            sh_move(f"{self._folder['FULL_PATH']}/{content}", f"{destiny}/{content}")
            
    #It will copy the contents of the folder to the destiny and will check if a folder or a file
    def copycontents(self, destiny:str, exceptions:list=None) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to copy the contents.")

        contents = self.list()
        
        if exceptions:
            for exception in exceptions:
                if exception in contents:
                    contents.remove(exception)

        for content in contents:
            if osp_isdir(f"{self._folder['FULL_PATH']}/{content}"):
                sh_copytree(f"{self._folder['FULL_PATH']}/{content}", f"{destiny}/{content}")
            elif osp_isfile(f"{self._folder['FULL_PATH']}/{content}"):
                sh_copyfile(f"{self._folder['FULL_PATH']}/{content}", f"{destiny}/{content}")
                  
    #It will list all the contents of the folder
    def list(self) -> list:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to list the contents.")

        return os_listdir(f"{self._folder['FULL_PATH']}")
        
    #It will count all the contents inside the folder
    def count(self) -> int:
        if not self.exists():
            raise FileNotFoundError("There is no such folder to count the contents.")

        return sum(1 for _ in self.list())

    #It will return True if the folder exists
    def exists(self) -> bool:
        return osp_isdir(f"{self._folder['FULL_PATH']}")
  
    #A dialog to select a folder will appear after that it will setup and separate the parent folder and folder name 
    def select(self, title:str="Select a folder", initialdir:str=None, mustexist:bool=False) -> bool:
        """It can return a boolean value to indicate if the folder was selected or not."""
        selected_folder = folderselect(title=title, initialdir=initialdir, mustexist=mustexist)
        if selected_folder != "":
            self._folder["FOLDER"] = selected_folder.split("/")[-1]
            self._folder["PARENT"] = "/".join(selected_folder.split("/")[:-1])+"/"
            self._update()
            return True
        else:
            return False
        
    #It will get the folder total size and return it in bytes
    def size(self, formated:bool=False) -> int:
        """Returns folder size in bytes or formated."""
        return foldersize(self._folder["FULL_PATH"], formated)
    
#Select Folder
def folderselect(title:str="Select a folder", initialdir:str=None, mustexist:bool=False) -> str:
    """It can return a string value to indicate the folder selected or None if the user cancels the dialog."""
    return outk_dialog("Directory", title=title, initialdir=initialdir, mustexist=mustexist)

#Folder Size
def foldersize(folder:str, autoformat:bool=True) -> int:
    """It can return a int value to indicate the size of the folder in bytes."""
    if not osp_isdir(folder):
        raise FileNotFoundError("There is no such folder to get the size.")
    
    size = 0
    for path, dirs, files in os_walk(folder):
        for file in files:
            filepath = osp_join(path, file)
            size += osp_getsize(filepath)
    
    if autoformat:
        size = ouo_formatsize(size)
    return size