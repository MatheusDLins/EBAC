'''
São erros que ocorrem durante a execução do código. O trecho do código **é** executado até o erro 'estourar'.

Erros por uso incorreto de tipos de dados. 'Estoura' exceção. Podem ser manipulados ou passados para frente (`raise`).
'''
preco = 132.85
pessoas = 0

valor_por_pessoa = preco / pessoas


# - **Exemplo**: Erro por combinações de tipos diferentes

nome = 'Andre Perez'
idade = True

apresentacao = 'Fala pessoal, meu nome é ' + \
    nome + ' e eu tenho ' + idade + ' anos'

# - **Exemplo**: Erro de indexação de estrutura de dados

anos = [2019, 2020, 2021]

ano_atual = anos[3]
print(ano_atual)

cursos = {
    'python': {
        'nome': 'Python para Análise de Dados', 'duracao': 2.5
    },
    'sql': {
        'nome': 'SQL para Análise de Dados', 'duracao': 2
    }
}


curso_atual = cursos['python']
print(curso_atual)

curso_atual = cursos['sql']
print(curso_atual)

curso_atual = cursos['analista']
print(curso_atual)


# **Erros de lógica**. Não 'estoura' exceção. A melhor forma de analise é usar a função `print` para verificar resultados intermediários.

#   * **Exemplo**: Loops infinitos.
controle = 0
while True:
    ...
    controle += 1
    if controle > 10:
        break

s = []
while True:
    s = s + (['CURSO DE PYTHON PARA ANALISE DE DADOS DA EBAC']
             * (1000 * 1000 * 1000))

# - **Exemplo**: Limites de coleções.

carrinho_compras = [{'id': 3184, 'preco': 37.65, 'qtd': 10}, {
    'id': 1203, 'preco': 81.20, 'qtd': 2}, {'id': 8921, 'preco': 15.90, 'qtd': 2}]

valor_total = 0
for indice in range(1, len(carrinho_compras)):
    valor_total += carrinho_compras[indice]['preco'] * \
        carrinho_compras[indice]['qtd']

valor_total = round(valor_total, 2)
print(valor_total)

valor_total = 0
for produto in carrinho_compras:
    valor_total += produto['preco'] * produto['qtd']

valor_total = round(valor_total, 2)
print(valor_total)

valor_total = 0
for indice in range(1, len(carrinho_compras)):
    print(carrinho_compras[indice])
    valor_total += carrinho_compras[indice]['preco'] * \
        carrinho_compras[indice]['qtd']

valor_total = round(valor_total, 2)
print(valor_total)
