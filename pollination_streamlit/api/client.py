import os
from pollination_io.api.client import ApiClient as ApiClientIO
from warnings import warn

DEFAULT_HOST = os.getenv('POLLINATION_API_URL',
                         'https://api.pollination.cloud')


class ApiClient(ApiClientIO):
    
    def __init__(self, host: str = DEFAULT_HOST, api_token: str = None, jwt_token: str = None):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(host=host,
                         api_token=api_token,
                         jwt_token=jwt_token)
