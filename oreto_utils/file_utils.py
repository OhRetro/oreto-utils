#File(s)

from os import remove as os_remove, rename as os_rename
from os.path import isfile as osp_isfile, getsize as osp_getsize, isdir as osp_isdir, abspath as osp_abspath
from shutil import move as sh_move, copy as sh_copy
from oreto_utils.tkinter_utils import filedialog as outk_filedialog

__all__ = ["File", "Files"]

class File:
    def __init__(self, file:str, path:str="./"):
        self._file = {
            "FILE": file,
            "NAME": None,
            "EXT": None,
            "PATH": path,
            "FULL_PATH": None,
            "TARGET": None,
            }
        self._update()
        
    #It will update the file path, file name and file extension
    def _update(self) -> None:
        #Check if the file path have "\" to replace with "/"        
        if "\\" in self._file["PATH"]:
            self._file["PATH"] = self._file["PATH"].replace("\\", "/")

        #Check if the file name have "\" or "/" to replace with "_"
        if "\\" in self._file["FILE"]:
            self._file["FILE"] = self._file["FILE"].replace("\\", "_")
        if "/" in self._file["FILE"]:
            self._file["FILE"] = self._file["FILE"].replace("/", "_")

        #Check if file itself has "." to separate the file name and file extension
        if "." in self._file["FILE"]:
            btndots = self._file["FILE"].split(".")

            self._file["NAME"] = btndots[0]
            if self._file["FILE"].find(".") > 1:
                for _ in btndots:
                    if _ not in [btndots[0], btndots[-1]]:
                        self._file["NAME"] += f".{_}"
            self._file["EXT"] = f".{btndots[-1]}"

        else:
            self._file["NAME"] = self._file["FILE"]

        self._file["FULL_PATH"] = osp_abspath(self._file["PATH"]).replace("\\", "/")
        self._file["TARGET"] = f"{self._file['FULL_PATH']}/{self._file['FILE']}"
    
    #It will rename the file name
    def rename(self, newname) -> None:
        """It will rename the file name."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to rename.")
        
        old_file = self._file["TARGET"]
        self._file["FILE"] = f"{newname}{self._file['EXT']}"
        self._update()
        
        os_rename(old_file, self._file["TARGET"])
        
    #It will return the file content
    def read(self) -> str:
        """It will return the file content."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to read.")
        
        with open(self._file["TARGET"], "r") as f:
            f_content = f.read()
            f.close()
            return f_content
    
    #It will return a specified line of the file content
    def readline(self, line:int) -> str:
        """It will return a specified line of the file content."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to read.")

        with open(self._file["TARGET"], "r") as f:
            f_content = f.readlines()
            f.close()
            return f_content[line]
        
    #It will write the content in the file and will overwrite the content if the file already exists
    def write(self, data:any="") -> None:
        """It will write the content in the file and will overwrite the content if the file already exists."""
        with open(self._file["TARGET"], "w", encoding="utf_8") as f:
            f.write(data)
            f.close()
            
    #It will append the content to the file
    def append(self, data:any="") -> None:
        """It will append the content to the file."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to append.")

        with open(self._file["TARGET"], "a", encoding="utf_8") as f:
            f.write(data)
            f.close()
                    
    #It will delete the file
    def delete(self) -> None:
        """It will delete the file."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to delete.")

        os_remove(f"{self._file['TARGET']}")

    #It will move the file to the destiny path
    def move(self, destiny:str) -> None:
        """It will move the file to the destiny path."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to move.")

        old_path = self._file["TARGET"]
        self._file["PATH"] = destiny
        self._update()

        sh_move(old_path, destiny)
        
    #It will copy the file to the destiny path
    def copy(self, destiny:str) -> None:
        """It will copy the file to the destiny path."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to copy.")

        if not osp_isdir(destiny):
            raise NotADirectoryError("There is no such directory to copy the file into.")
        
        sh_copy(self._file["TARGET"], destiny)
        
    #It will return True if the file exists
    def exists(self) -> bool:
        """It will return True if the file exists."""
        return osp_isfile(f"{self._file['TARGET']}")
    
    #A dialog to select a file will appear after that it will setup and separate the file path, the file name and file extension 
    def select(self, title:str="Select a file", initialdir:str=None, filetypes:list[tuple]=None) -> bool:
        """It can return a boolean value to indicate if the file was selected or not."""
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
            
        selected_file = outk_filedialog("FileName", title=title, initialdir=initialdir, filetypes=filetypes)
        
        if selected_file != "":
            self._file["FILE"] = selected_file.split("/")[-1]
            self._file["PATH"] = "/".join(selected_file.split("/")[:-1])
            self._update()
            return True
        else:
            return False
                
    #It will get the file total size return it in bytes
    def size(self) -> int:
        """It will return the file total size in bytes."""
        if not self.exists():
            raise FileNotFoundError("There is no such file to get the size.")

        return osp_getsize(self._file["TARGET"])
        
class Files:
    def select(title:str="Select a file", initialdir:str=None, filetypes:list[tuple]=None, multiple:bool=True) -> (tuple | str):
        """
        If the multiple argument is True, it will return a tuple with the selected files even if there is one file selected.\n
        Else, it will return a string with the selected file.
        """
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
            
        return outk_filedialog("FileName", title=title, initialdir=initialdir, filetypes=filetypes, multiple=multiple)