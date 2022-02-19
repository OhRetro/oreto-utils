#Terminal

from os import name, system
if name == "nt": import ctypes

class Terminal:
    #Clear the terminal
    def clear():
        if name == "nt": system("cls")
        else: system("clear")
        
    #Set title of the terminal
    def title(title:str):
        if name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(title)

    #Execute a command
    def execute(command:str):
        system(command)