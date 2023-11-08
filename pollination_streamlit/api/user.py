import typing as t

from .client import ApiClient
from pollination_io.api.user import UserApi as UserAPIIO
from warnings import warn


class UserApi(UserAPIIO):
    
    def __init__(self, client: ApiClient):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(client=client)

    def get_user(self) -> dict:
        return self.client.get('/user')
