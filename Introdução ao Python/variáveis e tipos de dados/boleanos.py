# Definição
# Armazenam valores lógicos:

# True (verdadeiro);
# False (falso).

verdadeiro = True
print(verdadeiro)

falso = False
print(falso)

# Tipo bool
print(type(True))

'''
São resultados de comparações lógicas. Os operadores de comparação lógica são:

*   `>` (maior);
*   `<` (menor);
*   `==` (igual);
*   `>=` (maior ou igual);
*   `<=` (menor ou igual);
*   `!=` (diferente).
'''

saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

'''
As operações de variáveis booleanas são: 

* `|` (operador ou)
* `&` (operador e)
* `not` (operador não)


O conjunto de resultados de operações lógicas geralmente é resumido em uma tabela chamada "tabela da verdade":
| A        | B        | | | A OR B   | | A AND B  | | NOT A    |
|----------|----------|-|-|----------|-|----------|-|----------|
|   TRUE   |   TRUE   | | |   TRUE   | |   TRUE   | |   FALSE  |
|   TRUE   |   FALSE  | | |   TRUE   | |   FALSE  | |   FALSE  |
|   FALSE  |   FALSE  | | |   FALSE  | |   FALSE  | |   TRUE   |
|   FALSE  |   TRUE   | | |   TRUE   | |   FALSE  | |   TRUE   |
'''

# Exemplo: Tabela da verdade do operador `|` (ou).
print(True | True)
print(True | False)
print(False | False)
print(False | True)

# Exemplo: Tabela da verdade do operador `&` (e).
print(True & True)
print(True & False)
print(False & False)
print(False & True)

# Exemplo: Tabela da verdade do operador `not` (não).
print(not True)
print(not False)

# conversão
# Podemos converter tipos numéricos e *strings* para booleanos através do método nativo `bool`:

idade = 19
tipo_sangue = 'O-'
filhos = 0
telefone_fixo = None
telefone_fixo = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo))
