#Definição
#Armazenam textos:

nome_aula = 'Aula 04, Módulo 01, Strings'

print(nome_aula)
print(type(nome_aula))

string_vazia = ""

print(string_vazia)
print(type(string_vazia))


#Operações
# + (concatenação).

nome = 'Andre Marcos'
sobrenome = 'Perez'

apresentacao = 'Olá, meu nome é ' + nome + ' ' + sobrenome + '.'
print(apresentacao)

nome = 'Andre Marcos'
sobrenome = 'Perez'

apresentacao = f'Olá, meu nome é {nome} {sobrenome}.'
print(apresentacao)

#Outra operação muito utilizada é a de fatiamento (*slicing*):

email = 'andre.perez@gmail.com'

print('0: ' + email[0])
print('11: ' + email[11])

print('-1: ' + email[-1])
print('-2: ' + email[-2])

#intervalo

email_usuario = email[0:11]
print(email_usuario)

email_provedor = email[12:21]
print(email_provedor)


#Metodos
#São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com *strings*:

endereco = 'Avenida Paulista, 1811, São Paulo, São Paulo, Brasil.'

# maiusculo: string.upper()
print(endereco.upper())

# posicao: string.find(substring)
posicao = endereco.find('Brasil')
print(posicao)

# substituição: string.replace(antigo, novo)
print(endereco.replace('Avenida', 'Av'))


#Conversão
idade = 19
print(type(idade))

idade = str(idade)
print(type(idade))

faturamento = 'R$ 35 mi'
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))