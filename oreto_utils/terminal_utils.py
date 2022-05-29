#Terminal

from os import name as os_name, system as os_system
import sys
if os_name == "nt": import ctypes

class Terminal:
    #Clear the terminal
    def clear():
        """Clear the terminal."""
        if os_name == "nt": os_system("cls")
        else: os_system("clear")
    
    #Clear the previous lines or the last line
    def clearlines(lines:int=1):
        """Clear the previous lines or the last line (Windows only for now)"""
        for _ in range(lines):
            if os_name == "nt":
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
     
    #Set title of the terminal
    def title(title:str):
        """Set title of the terminal (Windows only)"""
        if os_name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(title)