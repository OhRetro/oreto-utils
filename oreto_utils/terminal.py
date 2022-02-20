#Terminal

from os import name as os_name, system as os_system
if os_name == "nt": import ctypes

class Terminal:
    #Clear the terminal
    def clear():
        if os_name == "nt": os_system("cls")
        else: os_system("clear")
        
    #Set title of the terminal
    def title(title:str):
        if os_name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(title)

    #Execute a command
    def execute(command:str):
        os_system(command)