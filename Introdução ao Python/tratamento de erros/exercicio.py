# 0\. Preparação do ambiente
emprestimos = []
with open('./EBAC/Introdução ao Python/tratamento de erros/credito.csv', mode='r', encoding='utf8') as fp:
    fp.readline()  # cabeçalho
    linha = fp.readline()
    while linha:
        linha_emprestimo = {}
        linha_elementos = linha.strip().split(sep=',')
        linha_emprestimo['id_vendedor'] = linha_elementos[0]
        linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
        linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
        linha_emprestimo['data'] = linha_elementos[3]
        emprestimos.append(linha_emprestimo)
        linha = fp.readline()


for emprestimo in emprestimos:
  print(emprestimo)


### 1\. Função `map`
'''
Aplique a função map na lista de `emprestimos` para extrair os valores da chave `valor_emprestimos` na lista `valor_emprestimos_lista`. Faça também a conversão de `str` para `float`.

valor_emprestimos_lista = ...
'''

print(valor_emprestimos_lista) # [448.0, 826.7, ..., 4039.0]


### 2\. Função `filter`

'''Aplique a função filter na lista de `valor_emprestimos_lista` para filtrar apenas os valores maiores que zero (os valores negativas são erros na base de dados). Salve os valores na lista `valor_emprestimos_lista_filtrada`.'''

#valor_emprestimos_lista_filtrada = ...

#print(valor_emprestimos_lista_filtrada) # [448.0, 826.7, ..., 4039.0]

'''
3\. Função `reduce`

3\.1\. Função `reduce` para extrair a **soma**

Aplique a função reduce para somar os elementos da lista `valor_emprestimos_lista_filtrada` na variavel `soma_valor_emprestimos`.
'''

from functools import reduce

soma_valor_emprestimos = ...

print(soma_valor_emprestimos) # 14872.550000000001

#### 3\.2\. Função `reduce` para extrair a **media aritimética**

'''Aplique a função reduce para extrair a média aritimética dos elementos da lista `valor_emprestimos_lista_filtrada` na variavel `media_valor_emprestimos`.

Dica: Para calcular o tamanho da lista, isto é a quantidade de elementos, utilize a função len(), dentro do argumento da função coloque a lista `valor_emprestimos_lista_filtrada`.'''


from functools import reduce

media_valor_emprestimos = ...

print(media_valor_emprestimos) # 1859.0687500000001

#### 3\.3\. (**Desafio**) Função `reduce` para extrair o **desvio padrão amostral**
'''
Aplique a função reduce para extrair a média aritimética dos elementos da lista `valor_emprestimos_lista_filtrada` na variavel `desvio_padrao_valor_emprestimos`.'''

from functools import reduce

desvio_padrao_valor_emprestimos = ...

print(desvio_padrao_valor_emprestimos) # 1271.997271149785