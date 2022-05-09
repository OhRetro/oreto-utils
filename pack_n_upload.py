#!/usr/bin/python3

from os import system
from os import name
from time import sleep
from shutil import rmtree

_to_delete = ["build", "dist", "oreto_utils.egg-info"]

def pack():
    system("python setup.py sdist bdist_wheel")
    
def upload():
    system("twine upload dist/*")

def clean():
    sleep(2)
    for _ in _to_delete:
        rmtree(f"./{_}")

def clterm():
    if name == "nt":
        system("cls")
    else:
        system("clear")

if __name__ == "__main__":
    clterm()
    
    while True:
        print("="*50)
        print("1.pack+upload\n2.pack+upload+clean\n3.pack\n4.upload\n5.clean\n0.exit")
        _inp = int(input(">"))
        print("")

        if _inp in {1,2,3}:
            pack()
        if _inp in {1,2,4}:
            upload()
        if _inp in {2,5}:
            clean()
        if _inp == 0:
            clterm()
            break

        clterm()