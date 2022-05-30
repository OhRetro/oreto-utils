#JSON

import json
from oreto_utils.file_utils import File

class JSON:
    def __init__(self, jsonfile:str, path:str="./"):
        jsonfile = jsonfile.removesuffix(".json")
        self.json_file = File(jsonfile, ".json", path)
    
    #It will return the whole json file content
    def read(self) -> dict:
        return json.loads(self.json_file.read())
    
    #It will get a specified key from the json file
    def getkey(self, key:str) -> any:
        if "." not in key:
            return self.read()[key]

        _extrakeys = key.split(".")
        _key = self.read()[_extrakeys[0]]
        del _extrakeys[0]
        try:
            for extra in _extrakeys:
                _currentkey = extra
                _key = _key[extra]
        except KeyError as e:
            raise KeyError(f"The key \"{_currentkey}\" does not exist") from e

        return _key
    
    #It will set a specified key in the json file
    def setkey(self, key:str, value:any, overwrite:bool=False) -> None:
        json_dict = self.read()

        if "." not in key:
            json_dict[key] = value
        else:
            _extrakeys = key.split(".")
            _key = json_dict[_extrakeys[0]]
            del _extrakeys[0]

            pos = -1
            while True:
                if _extrakeys[pos] == _extrakeys[-1]:
                    _key[_extrakeys[pos]] = value
                    break
                
                _key = _key[_extrakeys[pos]]
                pos += 1

        self.json_file.write(json.dumps(json_dict), True)
    
    #It will delete a specified key from the json file
    def delkey(self, key:str) -> None:
        json_dict = self.read()

        if "." not in key:
            del json_dict[key]
        else:
            _extrakeys = key.split(".")
            _key = json_dict[_extrakeys[0]]
            del _extrakeys[0]

            pos = -1
            while True:
                if _extrakeys[pos] == _extrakeys[-1]:
                    del _key[_extrakeys[pos]]
                    break
                
                _key = _key[_extrakeys[pos]]
                pos += 1

        self.json_file.write(json.dumps(json_dict), True)

    #It will check if the key exists in the json file
    def existskey(self, key:str) -> bool:
        try:
            if self.getkey(key) is not None:
                return True
        except KeyError:
            return False