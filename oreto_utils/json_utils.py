#JSON

from json import loads as json_loads, dumps as json_dumps
from oreto_utils.file_utils import File as ouf_File

__all__ = ["JSON"]

class JSON:
    def __init__(self, file:str, path:str="./", separator:str="."):
        self._json = {
            "FILE": ouf_File(file, path),
            "SEPARATOR": separator
        }
        
        #Checks if the file is a json file
        if self._json["FILE"]._file["EXT"] != ".json":
            raise ValueError("The file is not a json file.")
    
    #Loads the json file
    def load(self) -> dict:
        """Loads the json file"""
        return json_loads(self._json["FILE"].read())
    
    #Gets the value of a key
    def getkey(self, key:str) -> any:
        """Gets the value of a key"""
        json_dict = self.load()
        
        if self._json["SEPARATOR"] not in key:
            return json_dict[key]

        og_key = key
        extrakeys = key.split(self._json["SEPARATOR"])
        
        try:
            for extrakey in extrakeys:        
                current_key = extrakey
                key = json_dict[extrakey] if extrakeys.index(current_key) == 0 else key[extrakey]

            return key

        except KeyError as e:
            raise KeyError(f"The key \"{current_key}\" in \"{og_key}\" does not exist.") from e

    #Sets the value of a key
    def setkey(self, key:str, value:any) -> None:
        """Sets the value of a key"""
        json_dict = self.load()

        if self._json["SEPARATOR"] not in key:
            json_dict[key] = value
        
        else:
            extrakeys = key.split(self._json["SEPARATOR"])
            
            for extrakey in extrakeys:
                current_key = extrakey
                                
                if extrakey == extrakeys[-1]:
                    key[extrakey] = value
                    break
                
                try:
                    if extrakeys.index(current_key) == 0:
                        key = json_dict[current_key]
                    else:
                        key = key[current_key]
                    
                except KeyError:
                    if extrakeys.index(current_key) == 0:
                        json_dict[current_key] = {}
                        key = json_dict[current_key]
                    else:
                        key[current_key] = {}
                        key = key[current_key]
                    
        self._json["FILE"].write(json_dumps(json_dict))
    
    #Deletes a key
    def deletekey(self, key:str) -> None:
        """Deletes a key"""
        json_dict = self.load()
        print(json_dict)
        if self._json["SEPARATOR"] not in key:
            json_dict.pop(key)
        else:
            extrakeys = key.split(self._json["SEPARATOR"])
            for extrakey in extrakeys:
                current_key = extrakey

                if current_key == extrakeys[-1]:    
                    key.pop(current_key)
                    break

                else:
                    if extrakeys.index(current_key) == 0:
                        key = json_dict[current_key]
                    else:
                        key = key[current_key]


        print(json_dict)
        self._json["FILE"].write(json_dumps(json_dict))

    #Checks if a key exists
    def existskey(self, key:str) -> bool:
        """Checks if a key exists"""
        try:
            if self.getkey(key) is not None:
                return True
        except KeyError:
            return False
    
    #Returns what type of the value of a key is
    def keytype(self, key:str) -> any:
        """Returns what type of the value of a key is"""
        try:
            return type(self.getkey(key))
        except KeyError:
            return None