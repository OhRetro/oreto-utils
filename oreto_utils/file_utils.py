#File(s)

from os import remove as os_remove, rename as os_rename, listdir as os_listdir
from os.path import isfile as osp_isfile, getsize as osp_getsize, isdir as osp_isdir, abspath as osp_abspath
from shutil import move as sh_move, copy as sh_copy
from oreto_utils.tkinter_utils import filedialog as outk_filedialog

__all__ = ["File", "Files"]

class File:
    def __init__(self, filename, fileext, filepath="./"):
        self.filename = filename
        self.filepath = filepath
        self.fileext = fileext
        self._update()
        
    #It will update the file path, file name and file extension
    def _update(self) -> None:
        #Check if the file path have "\" to replace with "/"        
        if "\\" in self.filepath:
            self.filepath = self.filepath.replace("\\", "/")
        
        #Check if the file path ends with "/"
        if not self.filepath.endswith("/"):
            self.filepath = f"{self.filepath}/"

        #Check if the file extension starts with "."
        if not self.fileext.startswith(".") and self.fileext != "":
            self.fileext = f".{self.fileext}"

        self.file = self.filepath+self.filename+self.fileext
        self.file_full_path = osp_abspath(self.file).replace("\\", "/")
                
    #It will rename the file name
    def rename(self, new_filename) -> None:
        old_file = self.file
        self.filename = new_filename
        self._update()
        os_rename(old_file, self.file)
        
    #It will return the file content
    def read(self) -> str:
        if not self.exists():
            raise FileNotFoundError("There is no such file to read.")
        
        with open(f"{self.file}", "r") as f:
            f_content = f.read()
            f.close()
            return f_content
    
    #It will return a specified line of the file content
    def readline(self, line_number:int) -> str:
        if not self.exists():
            raise FileNotFoundError("There is no such file to read.")

        with open(f"{self.file}", "r") as f:
            f_content = f.readlines()
            f.close()
            return f_content[line_number]
        
    #It will write the content in the file and can check if the file exists and if it does it will overwrite it or not
    def write(self, file_content="", overwrite:bool=True) -> None:
        if self.exists() and not overwrite:
            counter = sum(1 for _ in os_listdir(self.filepath) if _.startswith(self.filename) and _.endswith(self.fileext))
            self.rename(f"{self.filename} - Copy ({counter})")
            
        with open(f"{self.file}", "w") as f:
            f.write(file_content)
            f.close()
            
    #It will append the content to the file
    def append(self, file_content:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to append.")

        with open(f"{self.file}", "a") as f:
            f.write(file_content)
            f.close()
                    
    #It will delete the file
    def delete(self) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to delete.")

        os_remove(f"{self.file}")

    #It will move the file to the destiny path
    def move(self, path_destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to move.")

        old_path = self.file
        self.filepath = path_destiny
        self._update()

        sh_move(old_path, path_destiny)
        
    #It will copy the file to the destiny path
    def copy(self, path_destiny:str) -> None:
        if not self.exists():
            raise FileNotFoundError("There is no such file to copy.")

        if not osp_isdir(path_destiny):
            raise NotADirectoryError("There is no such directory to copy the file into.")
        
        sh_copy(self.file, path_destiny)
        
    #It will return True if the file exists
    def exists(self) -> bool:
        return osp_isfile(f"{self.file}")
    
    #A dialog to select a file will appear after that it will setup and separate the file path, the file name and file extension 
    def select(self, title:str="Select a file", initialdir:str=None, filetypes:list[tuple]=None) -> bool:
        """It can return a boolean value to indicate if the file was selected or not."""
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
        selected_file = outk_filedialog("FileName", title=title, initialdir=initialdir, filetypes=filetypes)
        if selected_file != "":
            self.filename = selected_file.split("/")[-1].split(".")[0]
            self.fileext = selected_file.split("/")[-1].split(".")[-1]
            self.filepath = "/".join(selected_file.split("/")[:-1])+"/"
            self._update()
            return True
        else:
            return False
                
    #It will get the file total size return it in bytes
    def size(self) -> int:
        if not self.exists():
            raise FileNotFoundError("There is no such file to get the size.")

        return osp_getsize(self.file)
        
class Files:
    def select(title:str="Select a file", initialdir:str=None, filetypes:list[tuple]=None, multiple:bool=True) -> (tuple | str):
        """
        If the multiple argument is True, it will return a tuple with the selected files even if there is one file selected.\n
        Else, it will return a string with the selected file.
        """
        if filetypes is None:
            filetypes = [("All Files (*.*)", "*.*")]
        return outk_filedialog("FileName", title=title, initialdir=initialdir, filetypes=filetypes, multiple=multiple)