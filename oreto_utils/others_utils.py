#Others

from oreto_utils.terminal_utils import clearlines as out_clearlines
from time import sleep as t_sleep

__all__ = ["countdown", "formatsize"]

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