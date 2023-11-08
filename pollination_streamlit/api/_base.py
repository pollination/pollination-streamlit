from .client import ApiClient
from pollination_io.api._base import APIBase as APIBaseIO
from warnings import warn

class APIBase(APIBaseIO):
    
    def __init__(self, client: ApiClient):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(client=client)
