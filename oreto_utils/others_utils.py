#Others

from terminal_utils import Terminal
from time import sleep as t_sleep

class Others:
    #This is a countdown
    def countdown(seconds:int, message:str="", endmessage:str=""):
        """
        This is a countdown that will print a message every second until it reaches 0.\n
        """
        while seconds > 0:
            print(f"{message} {seconds}")
            t_sleep(1)
            seconds -= 1
            Terminal.clearlines(1)
        print(endmessage)            
    
    #This wait for a value be equal to a certain value
    def untilequal(value:int, be_equal:int, name:str):
        """
        IT MAY NOT BE IN THE NEXT VERSION.\n\N
        Wait for a value to be equal to a certain value.\n
        This is meant to be used for watching a value if that value is in a multiprocess action.
        """
        while value != be_equal:
            print(f"Waiting for {name}: {value}/{be_equal}")
            Terminal.clearlines()
        print("[Done]\n")
    
    #This will transform a byte size in Kb, Mb, Gb, Tb or Pb 
    def formatsize(byte_size:int, return_as:str="unit"):
        """
        The size in byte will be transformed in Kb, Mb, Gb, Tb or Pb.\n
        You can choose whether you want to be returned as a unit (1 Mb) or as a number.
        """
        if return_as not in ["unit", "number"]:
            raise ValueError("The return_as argument must be 'unit' or 'number'.")

        if byte_size < 1024:
            selected_unit = 0
        elif byte_size < 1024**2:
            selected_unit = 1
        elif byte_size < 1024**3:
            selected_unit = 2
        elif byte_size < 1024**4:
            selected_unit = 3
        elif byte_size < 1024**5:
            selected_unit = 4
        else:
            selected_unit = 5

        if byte_size >= 1024:
            formated_size = float(f"{byte_size/1024**selected_unit:.2f}")
        else:
            formated_size = byte_size

        if return_as == "unit":
            units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
            return f"{formated_size} {units[selected_unit]}"
        elif return_as == "number":
            return formated_size