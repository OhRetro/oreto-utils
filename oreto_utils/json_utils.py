#JSON

from json import loads as json_loads, dumps as json_dumps
from oreto_utils.file_utils import File as ouf_File

__all__ = ["JSON"]

class JSON:
    def __init__(self, file:str, path:str="./", separator:str="."):
        self.file = ouf_File(file, path)
        
        #Checks if the file is a json file
        if self.file._file["ext"] != ".json":
            raise ValueError("The file is not a json file.")
        
        self.separator = separator
    
    #It will return the whole json file content
    def load(self) -> dict:
        return json_loads(self.file.read())
    
    #It will get a specified key from the json file
    def getkey(self, key:str) -> any:
        if self.separator not in key:
            return self.load()[key]

        _extrakeys = key.split(self.separator)
        _key = self.load()[_extrakeys[0]]
        del _extrakeys[0]
        try:
            for _extrakey in _extrakeys:
                _currentkey = _extrakey
                _key = _key[_extrakey]
        except KeyError as e:
            raise KeyError(f"The key \"{_currentkey}\" does not exist") from e

        return _key
    
    #It will set a specified key in the json file
    def setkey(self, key:str, value:any) -> None:
        json_dict = self.load()

        if self.separator not in key:
            json_dict[key] = value
        else:
            _extrakeys = key.split(self.separator)
            if not self.existskey(_extrakeys[0]):
                json_dict[_extrakeys[0]] = {}

            _key = json_dict[_extrakeys[0]]
            del _extrakeys[0]

            for _extrakey in _extrakeys:
                if _extrakey == _extrakeys[-1]:
                    _key[_extrakey] = value
                    break

                _key = _key[_extrakey]           

        self.file.write(json_dumps(json_dict), True)
    
    #It will delete a specified key from the json file
    def delkey(self, key:str) -> None:
        json_dict = self.load()

        if self.separator not in key:
            del json_dict[key]
        else:
            _extrakeys = key.split(self.separator)
            _key = json_dict[_extrakeys[0]]
            del _extrakeys[0]

            for _extrakey in _extrakeys:
                if _extrakey == _extrakeys[-1]:
                    del _key[_extrakey]
                    break
                
                _key = _key[_extrakey]

        self.file.write(json_dumps(json_dict), True)

    #It will check if the key exists in the json file
    def existskey(self, key:str) -> bool:
        try:
            if self.getkey(key) is not None:
                return True
        except KeyError:
            return False
    
    #It will get the key type from the json file
    def keytype(self, key:str) -> any:
        return type(self.getkey(key))