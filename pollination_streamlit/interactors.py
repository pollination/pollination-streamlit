import pathlib
import typing as t
from io import BytesIO
from uuid import UUID

from queenbee.io.inputs.job import JobArgument, JobPathArgument
from queenbee.job import Job as QbJob
from queenbee.job import JobArguments, JobStatus, RunStatus
from queenbee.recipe import Recipe as QbRecipe
from queenbee.recipe import RecipeInterface

from .api.client import ApiClient
from .dataframe import RunsDataFrame

from warnings import warn
from pollination_io.interactors import Recipe as RecipeIO
from pollination_io.interactors import Job as JobIO
from pollination_io.interactors import NewJob as NewJobIO
from pollination_io.interactors import Run as RunIO
from pollination_io.interactors import Artifact as ArtifactIO
from pollination_io.interactors import AuthUser as AuthUserIO


class Recipe(RecipeIO):

    def __init__(self, owner: str,
                 name: str,
                 tag: str = 'latest',
                 client: ApiClient = ApiClient()):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(owner=owner,
                         name=name,
                         tag=tag,
                         client=client)


class Job(JobIO):

    def __init__(self, owner: str, project: str, id: str, client: ApiClient = ApiClient()):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(owner=owner,
                         project=project,
                         id=id,
                         client=client)


class NewJob(NewJobIO):

    def __init__(self, owner: str, project: str, recipe: Recipe,
                 arguments: t.List[t.Dict[str, t.Any]] = [],
                 name: str = None, description: str = None,
                 client: ApiClient = ApiClient()):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(owner=owner,
                         project=project,
                         recipe=recipe,
                         arguments=arguments,
                         name=name,
                         description=description,
                         client=client)


class Run(RunIO):

    def __init__(self, owner: str, project: str, job_id: str, id: str, client: ApiClient = ApiClient()) -> None:
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(owner=owner,
                         project=project,
                         job_id=job_id,
                         id=id,
                         client=client)


class Artifact(ArtifactIO):

    def __init__(self, key: str, file_type: str, job: Job, **kwargs):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(key=key,
                         file_type=file_type,
                         job=job,
                         **kwargs)


class AuthUser(AuthUserIO):

    def __init__(self, client: ApiClient) -> None:
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(client=client)
