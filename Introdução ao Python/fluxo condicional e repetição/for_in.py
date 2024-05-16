# 3 Estrutura repetição for / in

# Estrutura que permite a execução repetida de um bloco de código repetidas vezes.

'''
for variavel_temporaria in coleção:
    <execute este código>
'''

for valor in range(6):
    print(valor)

soma = 0

for valor in range(0, 100000):
    soma = soma + valor
    # print(soma)

print(soma)

for multiplo_dois in range(2, 10, 3):
    print(multiplo_dois)

# 3.3. for / in / list
frutas = ['maca', 'banana', 'laranja', 'uva', 'pera']

for fruta in frutas:
    print(fruta)

frase = 'Fala pessoal, meu nome é André Perez.'

for caracter in frase:
    if (caracter == 'A') | (caracter == 'z'):
        print(f"A letra '{caracter}' está presente na frase.")

# 3.4 for / in / dict

credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
    print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.')
    print('\n')

for chave in credito.keys():
    print(chave)
    print(credito[chave])
    print(f'Para o documento {
          chave}, o valor do escore de crédito é {credito[chave]}.')
    print('\n')

for valor in credito.values():
    print(valor)
    print(f'O valor do escore de crédito é {
          valor}, mas não temos mais as chaves :(.')
    print('\n')

# 3.5. break / continue
for i in range(0, 10*10*10*10*10*10):
    print(i)
    if i == 10:
        break

numero = 3

if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')

numeros = [361, 553, 194, 13, 510, 33, 135]

for numero in numeros:

    if numero % 2 == 0:
        print(f'O numero {numero} é par')
        break
    else:
        print(f'O numero {numero} é impar')

numeros = [361, 553, 194, 13, 510, 33, 135]

for numero in numeros:

    if numero % 2 == 0:
        print(f'O numero {numero} é par')
        break
    else:
        continue
        print(f'O numero {numero} é impar')
