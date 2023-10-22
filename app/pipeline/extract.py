import os # para manipular arquivos e pastas
import glob # para listar arquivos
import pandas as pd
from typing import List

"""
    Função para ler os arquivos de uma pasta "data/input"
    e retornar uma lista de dataframes
    args: input_path (str): caminho da pasta
    return: list (list): lista de dataframes existentes no input_path
"""

path = 'data/input'

def extract_from_excel(path: str) -> List[pd.DataFrame]:

    all_files = glob.glob(f'{path}/*.xlsx')

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)

extract_from_excel(path)