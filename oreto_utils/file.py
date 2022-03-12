#File

from os import remove as os_remove
from os.path import isfile as osp_isfile
from shutil import move as sh_move

class File:
    def __init__(self, file_name="file", file_ext=".txt", file_path="./"):
        self.file_name = file_name
        
        #Check if the file path ends with "/"
        if not file_path.endswith("/"):
            file_path = f"{file_path}/"
        self.file_path = file_path

        #Check if the file extension starts with "."
        if not file_ext.startswith("."):
            file_ext = f".{file_ext}"
        self.file_ext = file_ext
        
        self.file = self.file_path+self.file_name+self.file_ext
    
    #Update File Properties
    def update_properties(self):
        if not self.file_path.endswith("/"):
            self.file_path = f"{self.file_path}/"

        if not self.file_ext.startswith("."):
            self.file_ext = f".{self.file_ext}"

        self.file = self.file_path+self.file_name+self.file_ext
        
    #Read file
    def read(self):
        if not self.exists():
            raise FileNotFoundError
        
        with open(f"{self.file}", "r") as f:
            f_content = f.read()
            f.close()
            return f_content
            
    #Write file
    def write(self, file_content=""):
        with open(f"{self.file}", "w") as f:
            f.write(file_content)
            f.close()
            
    #Delete file
    def delete(self):
        if not self.exists():
            return

        os_remove(f"{self.file}")

    #Move file
    def move(self, path_destiny:str):
        if not self.exists():
            raise FileNotFoundError

        sh_move(f"{self.file}", path_destiny)
        
    #Exists file
    def exists(self, print_output:bool=False):
        do_exists = osp_isfile(f"{self.file}")
        if print_output:
            if do_exists:
                print(f"{self.file} exists.")
            else:
                print(f"{self.file} does not exists")
        return do_exists