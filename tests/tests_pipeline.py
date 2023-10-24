import pandas as pd

from app.pipeline.transform import concatenate

df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def test_concatenar_lista_df():

    """

    Função para utilizar o arrange e act para testar a função concatenate
    
    """

    arrange = pd.concat([df1, df2], ignore_index=True)

    act = concatenate([df1, df2])

    assert arrange.equals(act)
