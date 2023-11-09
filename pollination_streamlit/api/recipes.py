
from pydantic import BaseConfig
from queenbee.recipe import Recipe

BaseConfig.allow_population_by_field_name = True

from .client import ApiClient
from pollination_io.api.recipes import RecipesAPI as RecipesAPIIO
from warnings import warn

class RecipesAPI(RecipesAPIIO):
    
    def __init__(self, client: ApiClient):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(client=client)
