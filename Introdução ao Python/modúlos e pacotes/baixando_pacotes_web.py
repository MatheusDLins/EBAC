'''
4. Baixando pacotes
4.1. PyPI
Repositório oficial de pacotes Python (link).
4.2. PIP
Ferramenta oficial para instalar pacotes Python armazenados no PyPI.
Instalando pacotes: pip install <pacote>==<versão>
'''

import json
import requests as req
'''!pip install requests == 2.25.1

# Listando pacotes: pip freeze

!pip freeze

!pip install - r requirements.txt

# Removendo pacotes: pip uninstall <pacote>

!pip uninstall requests'''


'''
4.3. Requests
Pacote para interação com o protocolo web HTTP (link).
Exemplo: Extrair a taxa CDI do site da B3
'''

response = req.get(
    'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'
)
print(f'status code: {response.status_code}')
print(response.text)
data = json.loads(response.text)
print(data)
print(type(data))

cdi = None
for key, value in data.items():
    if key == 'taxa':
        cdi = value.replace(',', '.')
        cdi = float(cdi)
print(cdi)
print(type(cdi))
