import pandas as pd
from typing import List

"""
função para transformar uma lista de dataframes em um único dataframe

args:

dataframe_list: list

"""

def concatenate(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframe_list, ignore_index=True)