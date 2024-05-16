# Definição
# Armazenam sequências no formato chave-valor. São do tipo `dict`.

brasil = {'capital': 'Brasília', 'idioma': 'Português', 'populacao': 210}

print(brasil)
print(type(brasil))


#Não é permite chaves duplicadas.
carro = {
    'marca': 'Volkswagen',
    'modelo': 'Polo',
    'ano': 2021,
    'ano': 2004
}

print(carro)

#Podemos criar dicionários compostos:
cadastro = {
    'andre': {
        'nome': 'Andre Perez', 
        'ano_nascimento': 1992, 
        'pais': {
            'pai': {
              'nome': '<nome-do-pai> Perez', 
              'ano_nascimento': 1971
            },
            'mae': {
              'nome': '<nome-da-mae> Perez', 
              'ano_nascimento': 1973
            },
        }
    }
}

print(cadastro)

cadastro['andre']['pais']['mae']['ano_nascimento']

#Operações

credito = {'123': 750, '789': 980}

#Elementos são acessados pela sua chave.
score_123 = credito['123']
score_789 = credito['789']

print(score_123)
print(score_789)

#Não é permite chaves duplicadas.
# Elementos são atualizados pela sua chave.
credito['123'] = 435
print(credito)

#Para adicionar um novo elemento, basta criar um novo elemento chave-valor:
credito['456'] = 1000
print(credito)

# métodos
artigo = dict(
    titulo='Modulo 02 | Python: Estruturas de Dados',
    corpo='Topicos, Aulas, Listas, Conjuntos, Dicionários, ...',
    total_caracteres=1530
)

# adicionar/atualizar um elemento pelo chave-valor: dict.update(dict)
print(artigo)
artigo.update({'total_caracteres': 7850})
print(artigo)

artigo['total_caracteres'] = 7850

# remover um elemento pelo chave: dict.pop(key)
print(artigo)
total_caracteres = artigo.pop('total_caracteres')
print(artigo)

#Conversão
artigo = dict(
    titulo='Modulo 02 | Python: Estruturas de Dados',
    corpo='Topicos, Aulas, Listas, Conjuntos, Dicionários, ...',
    total_caracteres=1530
)

chaves = list(artigo.keys())

print(chaves)
print(type(chaves))

valores = list(artigo.values())

print(valores)
print(type(valores))