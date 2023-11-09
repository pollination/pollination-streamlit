from .client import ApiClient
from pollination_io.api.runs import RunsAPI as RunsAPIIO
from warnings import warn

class RunsAPI(RunsAPIIO):
    
    def __init__(self, client: ApiClient):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(client=client)
