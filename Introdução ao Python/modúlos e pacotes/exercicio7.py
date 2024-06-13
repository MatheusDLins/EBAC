# pip install wget==3.2

import pandas as pd
import os
import zipfile
import wget

wget.download(
    url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')


with zipfile.ZipFile('./dados.zip', 'r') as fp:
    fp.extractall('./dados')


os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')

#!pip install pandas==1.1.5


df = pd.read_csv('./dados/dow_jones_index.csv')

df.head(n=10)

df.columns.to_list()

linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

df_mcd = df[df['stock'] == 'MCD']


df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

df_mcd.head(n=10)

df_mcd.dtypes

for col in ['open', 'high', 'low', 'close']:
    df_mcd[col] = df_mcd[col].apply(
        lambda value: float(value.split(sep='$')[-1]))

df_mcd.head(n=10)

df_mcd.dtypes
