#pip install wget==3.2

import wget

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

import zipfile

with zipfile.ZipFile('./dados.zip', 'r') as fp:
  fp.extractall('./dados')

import os

os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')

#!pip install pandas==1.1.5

import pandas as pd

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
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))

df_mcd.head(n=10)

df_mcd.dtypes

