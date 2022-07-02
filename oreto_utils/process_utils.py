#Process

from oreto_utils.terminal_utils import clearlines as out_clearlines
from oreto_utils.others_utils import countdown as ouo_countdown
from psutil import process_iter as ps_pi

__all__ = ["waitprocess", "isrunning", "killprocess"]

#Wait for a process to start/end
def waitprocess(process:str, waituntil:str, updaterate:int=1, afterwait=None) -> None:
    """
    Wait for a process to start/end.\n
    Valid waituntil values are "start" and "end".\n
    The afterwait argument is a function that will be called after the process has started/ended.\n
    """
    
    #Valid waituntil values
    VALID = ["start", "end"]
    if waituntil not in VALID:
        raise ValueError(f"The waituntil argument must be one of {VALID}")

    #Wait until the process is started
    elif waituntil == "start":
        for _ in range(999999):
            if process in [p.name() for p in ps_pi()]:
                break
            ouo_countdown(updaterate, message=f"Waiting \"{process}\" to start... Updating in ")
            out_clearlines(1)

    #Wait until the process is ended
    elif waituntil == "end":
        for _ in range(999999):
            if process not in [p.name() for p in ps_pi()]:
                break
            ouo_countdown(updaterate, message=f"Waiting \"{process}\" to end... Updating in ")
            out_clearlines(1)
            
    #Call the afterwait function
    if afterwait:
        afterwait.__call__()
 
#Check if a process is running
def isrunning(process:str) -> bool:
    process_list = [p.name() for p in ps_pi()]
    if process in process_list:
        return True
    return False

#Kill a process
def killprocess(process:str) -> None:
    for p in ps_pi():
        if p.name() == process:
            p.kill()
            break