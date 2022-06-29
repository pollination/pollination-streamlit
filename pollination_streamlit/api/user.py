import typing as t

from ._base import APIBase


class UserApi(APIBase):

    def get_user(self) -> dict:
        return self.client.get('/user')
