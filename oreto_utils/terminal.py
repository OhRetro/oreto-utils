#Terminal

from os import name as os_name, system as os_system
from keyboard import wait as kb_wait, press_and_release as kb_par
from sys import stdout
if os_name == "nt": import ctypes

__all__ = ["clear", "clearlines", "clearprevline", "title", "waitinput"]

#Clear the terminal
def clear() -> None:
    """Clear the terminal."""
    if os_name == "nt": os_system("cls")
    else: os_system("clear")

#Clear the previous lines or the last line
def clearlines(lines:int=1) -> None:
    """Clear the previous lines or the last line"""
    for _ in range(lines):
        stdout.write('\x1b[1A')
        stdout.write('\x1b[2K')

#Clear a specific line
def clearprevline(prevline:int=1) -> None:
    """Clear a specific previous line"""
    #Cursor goes up
    for _ in range(prevline):
        stdout.write('\x1b[1A')
    #Clear the line
    stdout.write('\x1b[2K')
    #Cursor goes down
    for _ in range(prevline):
        stdout.write('\x1b[1B')
            
#Set title of the terminal
def title(title:str) -> None:
    """Set title of the terminal (Windows only)"""
    if os_name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(title)
    
#Wait for keybord input press
def waitinput(key:str="enter", showmessage:bool=True, message:str="Press %key% to continue...", onrelease:bool=False) -> None:
    """
    Wait for keybord input press\n
    To use custom message you have to put \"%key%\" in the message so it will be replaced by the key. 
    """
    if showmessage: 
        print(message.replace("%key%", key.capitalize()))
    kb_wait(key, trigger_on_release=onrelease)
    kb_par("enter")
    input()
    clearlines()