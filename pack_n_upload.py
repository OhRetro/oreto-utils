#!/usr/bin/python3

from os import system
from os import name
from time import sleep
from shutil import rmtree

_to_delete = ["build", "dist", "oreto_utils.egg-info"]


def pack():
    system("python3 setup.py sdist bdist_wheel")
    
def upload():
    system("twine upload dist/*")

def clean():
    sleep(2)
    for _ in _to_delete:
        rmtree(f"./{_}")

if __name__ == "__main__":
    while True:
        if name == "nt": system("cls")
        else: system("clear")

        print("1.pack+upload\n2.pack+upload+clean\n3.pack\n4.upload\n5.clean")
        _inp = int(input(">"))

        if _inp in {1,2,3}: pack()
        if _inp in {1,2,4}: upload()
        if _inp in {2,5}: clean()