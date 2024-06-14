import seaborn as sns
import csv
from sys import argv
import os
import json
from datetime import datetime

import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

# Criando a variável data e hora

data_e_hora = datetime.now()
data = datetime.strftime(data_e_hora, '%Y/%m/%d')
hora = datetime.strftime(data_e_hora, '%H:%M:%S')

# Captando a taxa CDI do site da B3

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.HTTPError as exc:
    print("Dado não encontrado, continuando.")
    cdi = None
except Exception as exc:
    print("Erro, parando a execução.")
    raise exc
else:
    dado = json.loads(response.text)
    cdi = float(dado['taxa'].replace(',', '.'))

# Verificando se o arquivo "taxa-cdi.csv" existe

if os.path.exists('./taxa-cdi.csv') == False:

    with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
        fp.write('data,hora,taxa\n')

# Salvando dados no arquivo "taxa-cdi.csv"

with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
    fp.write(f'{data},{hora},{cdi}\n')

print("Sucesso")


# Vamos criar o arquivo de *script* `extrair-cdi.py`.

#!python extrair-cdi.py

# **Exemplo:** Script com argumentos.


print(argv)
print(type(argv))

# Vamos criar o arquivo de *script* `args.py`.

#!python args.py

# **Exemplo:** *Script* para gerar um grafico da taxa CDI do site da B3.


# Extraindo as colunas hora e taxa

horas = []
taxas = []

with open(file='./taxa-cdi.csv', mode='r', encoding='utf8') as fp:
    linha = fp.readline()
    linha = fp.readline()
    while linha:
        linha_separada = linha.split(sep=',')
        hora = linha_separada[1]
        horas.append(hora)
        taxa = float(linha_separada[2])
        taxas.append(taxa)
        linha = fp.readline()

# Salvando no grafico

grafico = sns.lineplot(x=horas, y=taxas)
grafico.get_figure().savefig(f"{argv[1]}.png")

# Vamos criar o arquivo de *script* `cdi-grafico.py`.

#!python cdi-grafico.py 'dia-10'

# **3.3. Ferramenta de Desenvolvimento Local**
'''
As IDEs (Integrated Development Environment) são ferramentas completas de desenvolvimento de código em software.

*   **PyCharm** da JetBrains ([link](https://www.jetbrains.com/));
*   **Visual Studio Code** da Microsoft ([link](https://code.visualstudio.com/)).
'''
