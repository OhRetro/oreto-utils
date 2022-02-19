#!/usr/bin/python3

from os import system
from oreto_utils import File
import json

if __name__ == "__main__":
    _file_path = "./credentials.json"
    if _file_exists := File.exists(_file_path):
        try:
            _file = json.loads(File.load(_file_path))
            
            system("python3 setup.py sdist bdist_wheel")
            system("twine upload dist/*")
            system(_file["user"])
            system(_file["password"])
        except Exception as _:
            print(_)

    else:
        print("\ncredentials.json not found, creating now.")
        try:
            File.create("./credentials.json", '{"user": "", "password": ""}')
        except Exception as _:
            print(f"an error has occurred:\n{_}\n")
        finally:
            print("credentials.json created successfully.")
        