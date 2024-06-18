import csv
from sys import argv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Extraindo as colunas hora e taxa

df = pd.read_csv('./taxa-cdi.csv')

# Salvando no gráfico
plt.figure(figsize=(10, 5))
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])

# Definir ticks explicitamente
grafico.set_xticks(range(len(df['hora'])))
grafico.set_xticklabels(labels=df['hora'], rotation=90)

# Verificar o argumento de linha de comando para o nome do arquivo
output_file = argv[1] if len(argv) > 1 else 'output.png'

grafico.get_figure().savefig(output_file)
