import typing as t
import pandas as pd
from pollination_io.dataframe import ColumnMeta as ColumnMetaIO
from pollination_io.dataframe import RunsDataFrame as RunsDataFrameIO
from warnings import warn

class ColumnMeta(ColumnMetaIO):

    def __init__(self, inputs: t.List[str] = [], outputs: t.List[str] = [],
                 parameters: t.List[str] = [], artifacts: t.List[str] = []):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(inputs=inputs,
                         outputs=outputs,
                         parameters=parameters,
                         artifacts=artifacts)


class RunsDataFrame(RunsDataFrameIO):

    def __init__(self, df: pd.DataFrame, meta: ColumnMeta = ColumnMeta):
        warn(f'{self.__class__.__name__} will be deprecated. Use pollination-io instead.', 
             DeprecationWarning, 
             stacklevel=2)
        super().__init__(df=df,
                         meta=meta)
