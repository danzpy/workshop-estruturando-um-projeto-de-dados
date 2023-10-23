import glob  # para listar arquivos
import os  # para manipular arquivos e pastas
from typing import List

import pandas as pd

path = 'data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:

    """
    Função para ler os arquivos de uma pasta "data/input"
    e retornar uma lista de dataframes
    args: input_path (str): caminho da pasta
    return: list (list): lista de dataframes existentes no input_path
    """

    all_files = glob.glob(f'{path}/*.xlsx')

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)

extract_from_excel(path)
