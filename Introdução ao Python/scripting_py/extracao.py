import os
import time
import json
from random import random
from datetime import datetime
import requests

URL = 'https://www.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

# Loop para capturar dados 10 vezes
for _ in range(0, 10):

    # Criando a variável data e hora
    data_e_hora = datetime.now()
    data = data_e_hora.strftime('%Y/%m/%d')
    hora = data_e_hora.strftime('%H:%M:%S')

    # Captando a taxa CDI do site da B3
    try:
        response = requests.get(URL,  verify=False)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        cdi = None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',', '.')) + (random() - 0.5)

    # Verificando se o arquivo "taxa-cdi.csv" existe
    if not os.path.exists('./taxa-cdi.csv'):
        with open('./taxa-cdi.csv', 'w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    # Salvando dados no arquivo "taxa-cdi.csv"
    with open('./taxa-cdi.csv', 'a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')

    # Pausa antes da próxima captura
    time.sleep(2 + (random() - 0.5))

print("Sucesso")
