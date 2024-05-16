# 1\. Estrutura condicional if / else / elif

# if / else

'''
if <booleano / comparação lógica> == True:
  <execute este código>
else:
  <senão execute este código>
'''

if False:
    print("Verdadeiro")
else:
    print("Falso")

codigo_de_seguranca = '291'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

if pode_efetuar_pagamento:
    print("Pagamento efetuado")
else:
    print("Erro: Código de segurança inválido")

if codigo_de_seguranca == codigo_de_seguranca_cadastro:
    print("Pagamento efetuado")
else:
    print("Erro: Código de segurança inválido")

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '852'

senha = '7783'
senha_cadastro = '7783'

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print("Pagamento efetuado")
else:
    print("Erro: Pagamento não efetuado")

if (codigo_de_seguranca != codigo_de_seguranca_cadastro) | (senha != senha_cadastro):
    print("Erro: Pagamento não efetuado")
else:
    print("Pagamento efetuado")

'''
if <1º booleano / 1ª comparação lógica> == True:
    <execute este código se a primeira condição for verdade>
elif <2º booleano / 2ª comparação lógica> == True:
    <execute este código se a segunda condição for verdade>
else:
    <senão execute este código>
'''

codigo_de_seguranca = '802'
codigo_de_seguranca_cadastro = '852'

senha = '7703'
senha_cadastro = '7783'

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print("Pagamento efetuado")

elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print("Erro: Código de segurança inválido")

elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha != senha_cadastro):
    print("Erro: Senha inválida inválida")

else:
    print("Erro: Código de segurança e senha inválidos")
