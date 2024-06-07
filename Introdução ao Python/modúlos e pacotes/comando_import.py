'''
1. from / import / as
Os módulos nativos do Python podem ser encontrados neste link.
1.1. import
Exemplo: random
'''
import random
escolha = random.choice([1, 2, 3])
print(escolha)
numero_aleatorio = random.random() # entre [0,1)
print(numero_aleatorio)

import math

potencia = math.pow(10, 10)
print(potencia)
num = math.ceil(10.1)
print(num)
print(math.pi)

'''
1.2. from, import
Exemplo: time
'''

from time import time
print(time())
sleep(5)
from time import time, sleep
sleep(5)


'''
1.3. from, import, as
Exemplo: datetime
'''

from datetime import datetime as dt
print(dt.now())
print(dt.now().day)
print(dt.now().year)
