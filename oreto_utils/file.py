#File
#0.1.1

from os import remove as os_remove
from os.path import isfile as osp_isfile
from shutil import move as sh_move
from configparser import ConfigParser
import json

class File:
    #Load/Read file
    def load(file_path:str):
        try:
            with open(file_path, "r") as _file:
                if _file.endswith(".json"):
                    return json.loads(_file.read())
                elif _file.endswith(".ini"):
                    return ConfigParser().read(file_path)
                else:
                    return _file.read()
        except FileNotFoundError:
            print(f"There is no '{file_path}' to load.")

    #Create/Write file
    def create(file_path:str, file_content:str=""):
        try:
            with open(f"{file_path}", "x") as _file:
                _file.write(file_content)
                _file.close()
        except FileExistsError:
            print(f"'{file_path}' already exists")
            
    #Overwrite file
    def overwrite(file_path:str, file_content:str=""):
        try:
            with open(f"{file_path}", "w") as _file:
                _file.write(file_content)
                _file.close()
        except FileNotFoundError:
            print(f"There is no '{file_path}' to overwrite.")
            
    #Delete/Remove file
    def delete(file_path:str):
        try:
            os_remove(f"{file_path}")
        except FileNotFoundError:
            print(f"There is no '{file_path}' to delete.") 

    #Move file
    def move(file_path:str, new_file_path:str):
        sh_move(file_path, new_file_path)
        
    #Exists file
    def exists(file_path:str, print_output:bool=False):
        do_exists = osp_isfile(file_path)
        if print_output:
            if do_exists:
                print(f"'{file_path}' exists.")
            else:
                print(f"'{file_path}' does not exists") 
        return do_exists