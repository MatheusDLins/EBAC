'''
Aplica uma função a todos os elemento de uma coleção, dois a dois, e retorna **apenas** um elemento.


variavel = reduce(função, coleção)
'''

numeros = [1, 2, 3]

from functools import reduce

soma = reduce(lambda x, y: x + y, numeros)
print(soma)


def maior_entre(primeiro: int, segundo: int) -> int:
  return primeiro if primeiro >= segundo else segundo

primeiro = 11
segundo = 11

print(maior_entre(primeiro=primeiro, segundo=segundo))

from random import random

print(random())

#from random import random

numeros = [round(100 * random()) for _ in range(0, 100)]
print(numeros)

maior_numero = reduce(maior_entre, numeros)
print(maior_numero)

maior_numero = reduce(lambda primeiro, segundo: primeiro if primeiro >= segundo else segundo, numeros)
print(maior_numero)



from random import random

numeros = [round(100 * random()) for _ in range(0, 100)]
print(numeros)

numeros_ao_quadrado = map(lambda numero: numero ** 2, numeros)

numeros_impares = filter(lambda numero: numero % 2 != 0, numeros_ao_quadrado)

soma_numeros = reduce(lambda x, y: x + y, numeros_impares)
print(soma_numeros)

soma_numeros = reduce(lambda x, y: x + y, filter(lambda numero: numero % 2 != 0, map(lambda numero: numero ** 2, numeros)))
print(soma_numeros)