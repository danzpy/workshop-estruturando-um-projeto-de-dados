import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:

    """
    Receber um dataframe e salva-lo com excel

    args:

    data_frame: pd.DataFrame: Dataframe a ser salvo
    output_path: (str): Caminho onde o arquivo será salvo
    file_name: (str): Nome do arquivo a ser salvo

    return: (str): "Arquivo salvo com sucesso"

    """

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)

    return 'Arquivo salvo com sucesso'
