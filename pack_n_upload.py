#!/usr/bin/python3

from os import system

if __name__ == "__main__":
    try:
        system("python3 setup.py sdist bdist_wheel")
        system("twine upload dist/*")
    except Exception as _:
        print(_)