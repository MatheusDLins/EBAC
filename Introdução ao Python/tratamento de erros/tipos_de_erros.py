# - **Erros de sintaxe**: erros que ocorrem durante a escrita do código.

idade = 19

'''
if idade > 18
  return True
  '''

# - **Erros em tempo de execução**: erros que ocorrem durante a execução do código.

#Erros de uso incorreto de tipos de dados.

print(1/0)

#Erros de lógica

i = 0
while True:
  ... # bloco de código
  i += 1
  if i > 10:
    break