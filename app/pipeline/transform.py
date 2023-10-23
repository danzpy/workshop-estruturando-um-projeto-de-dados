from typing import List

import pandas as pd


def concatenate(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:

    """
    função para transformar uma lista de dataframes em um único dataframe

    args:

    dataframe_list: list

    """

    return pd.concat(dataframe_list, ignore_index=True)
