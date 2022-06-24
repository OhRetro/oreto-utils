from os import system
from os import name
from time import sleep
from shutil import rmtree
from contextlib import suppress

_to_delete = ["build", "dist", "oreto_utils.egg-info"]
_version = "0.8"

def build():
    system("python setup.py sdist bdist_wheel --universal")
    
def upload():
    system("twine upload dist/*")

def clean():
    sleep(2)
    system("py ./setup.py clean")
    for _ in _to_delete:
        rmtree(f"./{_}")

def install():
    system(f"pip install -U ./dist/oreto-utils-{_version}.tar.gz")
    
def changeversion():
    global _version
    _version = input("Change version: ")

def clterm():
    if name == "nt":
        system("cls")
    else:
        system("clear")

if __name__ == "__main__":
    clterm()
    _valid = {1,2,3,4,5}
    _run = True
    while _run:
        print(f"ver: {_version}")
        print("1.build\n2.upload\n3.clean\n4.install build\n5.change ver\n0.exit\n")
        try:
            _inp = input(">")
            with suppress(Exception):
                _extr = _inp.split(" ")[1] if len(_inp.split(" ")) > 1 else ""
                _inp = _inp.split(" ")[0]
                _qq = [int(q) for q in _inp]
        except ValueError:
            _inp = -1
            continue

        print("")

        for q in _qq:
            _inp = q
            if _inp == 1:
                print("Building:")
                build()
            elif _inp == 2:
                print("Uploading:")
                upload()
            elif _inp == 3:
                print("Cleaning:")
                clean()
            elif _inp == 4:
                print("Installing:")
                install()
            elif _inp == 5:
                print("Changing:")
                changeversion()

            print("")
            if _inp == 0:
                clterm()
                _run = False
            elif _inp not in _valid or _extr not in ["keep", "k"]:
                clterm()