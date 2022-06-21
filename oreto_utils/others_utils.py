#Others

from oreto_utils.terminal_utils import clearlines as out_clearlines
from time import sleep as t_sleep

__all__ = ["countdown", "formatsize", "searchlist"]

#This is a countdown
def countdown(seconds:int, message:str="", endmessage:str="") -> None:
    """This is a countdown that will print a message every second until it reaches 0."""
    for _ in range(seconds):
        print(f"{message}{seconds}")
        t_sleep(1)
        seconds -= 1
        out_clearlines(1)
    print(endmessage)            
    
#This will format a byte size in KB, MB, GB, TB or PB 
def formatsize(bytesize:int) -> str:
    """The size in byte will be formated in KB, MB, GB, TB or PB."""
    if bytesize < 1024:
        selected_unit = 0
    elif bytesize < 1024**2:
        selected_unit = 1
    elif bytesize < 1024**3:
        selected_unit = 2
    elif bytesize < 1024**4:
        selected_unit = 3
    elif bytesize < 1024**5:
        selected_unit = 4
    else:
        selected_unit = 5

    if bytesize >= 1024:
        formated_size = round(bytesize/1024**selected_unit, 2)
    else:
        formated_size = round(bytesize)

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
    return f"{formated_size} {units[selected_unit]}"

#This searches for a specific value in a list, and returns the index of the value
#It will return None if the value is not found
def searchlist(list:list, search:any, mode:str) -> (list | int):
    """
    This searches for a specific value in a list, and returns the index of the value.
    It will return None if the value is not found.\n
    Modes:
        f: First
        l: Last
        c1: Contains (Returns index), c2: Contains (Returns a list of exactly which ones contains the search term)
        e: Exact
    """
    if search in list:
        VALID = ["f", "l", "c1", "c2", "e"]
        if mode not in VALID:
            raise ValueError(f"Mode {mode} is not valid. Valid modes are: {VALID}")
        elif mode == "f":
            items = [item for item in list if item.startswith(search)]
            return items[0]
        elif mode == "l":
            items = [item for item in list if item.startswith(search)]
            return items[-1]
        elif mode[0] == "c":
            if mode[1] == "1":
                return [list.index(items) for items in list if search in items]
            elif mode[1] == "2":
                return [items for items in list if search in items]
        elif mode == "e":
            return list.index(search)
    return None