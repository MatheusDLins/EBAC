'''
Função anônima (sem nome) com bloco de código super enxuto e que pode ser salva em uma variável. Em geral é utilizada com outros métodos funcionais como `map`, `filter`, e `reduce`.

variavel = lambda params: expressão
'''


def extrair_provedor_email(email): return email.split(sep='@')[-1]


email = 'andre.perez@gmail.com'
print(email)

provedor_email = extrair_provedor_email(email)
print(provedor_email)

# **Exemplo**: Função `lamba` com estruturas condicionais.


def numero_e_par(numero): return True if numero % 2 == 0 else False


numeros = range(0, 10)

for numero in numeros:
    if numero_e_par(numero) == True:
        print(f'O número {numero} é par!')


# **1.2. Função de alta ordem**


# São funções que recebem outras funções para parâmetro ou retornam outra função.

def retorno(juros: float):
    return lambda investimento: investimento * (1 + juros)


retorno_5_porcento = retorno(juros=0.05)
retorno_10_porcento = retorno(juros=0.10)

valor_final = retorno_5_porcento(investimento=1000)
print(valor_final)

valor_final = retorno_10_porcento(investimento=1000)
print(valor_final)


anos = 10
valor_inicial = 1000
valor_final = valor_inicial

for ano in range(1, anos+1):
    valor_final = retorno_5_porcento(investimento=valor_final)

valor_final = round(valor_final, 2)
print(valor_final)


anos = 10
valor_inicial = 1000
valor_final = valor_inicial

for ano in range(1, anos+1):
    valor_final = retorno_10_porcento(investimento=valor_final)

valor_final = round(valor_final, 2)
print(valor_final)
