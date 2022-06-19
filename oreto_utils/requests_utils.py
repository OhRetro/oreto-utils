#Requests

from requests import get as re_get
from requests.exceptions import ConnectionError

__all__ = ["rget"]

#It will make a request to the url and return the response, if the request fails it will return None
def rget(url:str, params:dict=None, headers:dict=None, timeout:int=None, **kwargs):
    try:
        return re_get(url=url, params=params, headers=headers, timeout=timeout, **kwargs)
    except ConnectionError:
        return None