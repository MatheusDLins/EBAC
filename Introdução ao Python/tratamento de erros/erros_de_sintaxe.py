# São erros que ocorrem durante a escrita do código. O trecho do código **não é** executado.
'''
carrinho_compras = [{'id': 3184, 'preco': 37.65, 'qtd': 10}, {'id': 1203, 'preco': 81.20, 'qtd': 2}, {'id': 8921, 'preco': 15.90, 'qtd': 2}]

**Exemplo**: Esquecer o 'dois pontos' `:` no final de estruturas de condição, repetição, etc.

for produto in carrinho_compras
  ...

**Exemplo**: Condição lógica no `else` da estrutura de decisão `if-elif-else`.

for produto in carrinho_compras:
  if produto['id'] == 3184:
    ...
  else produto['id'] == 1203:
    ...
'''
