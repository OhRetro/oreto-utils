#!/usr/bin/python3

from os import system
from os import name
from time import sleep
from shutil import rmtree

_to_delete = ["build", "dist", "oreto_utils.egg-info"]

def build():
    system("python setup.py sdist bdist_wheel")
    
def upload():
    system("twine upload dist/*")

def clean():
    sleep(2)
    system("py ./setup.py clean")
    for _ in _to_delete:
        rmtree(f"./{_}")

def install():
    system("py ./setup.py install")
    
def clterm():
    if name == "nt":
        system("cls")
    else:
        system("clear")

if __name__ == "__main__":
    clterm()
    while True:
        print("="*50)
        print("1.build+upload\n2.build+upload+clean\n3.build\n4.upload\n5.clean\n6.install build\n0.exit")
        try:
            _inp = int(input(">"))
        except ValueError:
            _inp = -1
            continue
        
        print("")

        if _inp in {1,2,3}:
            build()
        if _inp in {1,2,4}:
            upload()
        if _inp in {2,5}:
            clean()
        if _inp in {6}:
            install()
        print("")        
        if _inp == 0:
            clterm()
            break
        elif _inp < 0 or _inp > 6:
            clterm()
        clterm()