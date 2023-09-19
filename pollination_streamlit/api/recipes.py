
from pydantic import BaseConfig
from queenbee.recipe import Recipe

from ._base import APIBase

BaseConfig.allow_population_by_field_name = True


class RecipesAPI(APIBase):

    def get_recipe(self, owner: str, name: str, tag: str = 'latest') -> Recipe:
        res = self.client.get(
            path=f'/registries/{owner}/recipe/{name}/{tag}/json'
        )
        return Recipe.parse_obj(res)

    def add_to_project(self, owner: str, name: str,
                    project_slug: str, tag: str = 'latest') -> str:
        prj_owner, prj_name = project_slug.split('/')
        res = self.client.post(
            path=f'/projects/{prj_owner}/{prj_name}/recipes/filters',
            json={
                "owner": owner,
                "name": name,
                "tag": tag
            }
        )
        return res
