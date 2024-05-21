'''Comando para ler arquivos.
Comando para ler/escrever arquivos.

with open(file='<caminho do arquivo do arquivo>', mode='<modo de leitura/escrita>', encoding='<decodificador>') as <apelido>:
    bloco de código

Os modos de leitura são:

r: Abrir o arquivo para leitura (padrão);
w: Abrir o arquivo para escrita (sobreescreve o arquivo original).
a: Abrir o arquivo para acrescentar (não sobreescreve o arquivo original)



'''

idades = []

with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        # quebra a string nas virgulas(ponto e virgula) e salva os resultados em uma lista
        linha_separada = linha.split(sep=';')
        idade = linha_separada[0]  # seleciona o primeiro elemento da lista
        idade = int(idade)  # converte o valor de string para integer (inteiro)
        idades.append(idade)  # salva o valor na lista de idades
        # lê uma nova linha, se a linha não existir, salva o valor None
        linha = arquivo.readline()

# write (w)

with open(file='idades.csv', mode='w', encoding='utf8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha)

# Modo de acréscimo (a)
with open(file='idades.csv', mode='a', encoding='utf8') as fp:
    for idade in idades:
        linha = str(idade + 100) + '\n'
        fp.write(linha)


#copiando
with open(file='./banco.csv', mode='r', encoding='utf8') as leitura:
    with open(file='./banco-csv.csv', mode='w', encoding='utf8') as escrita:
        linha = leitura.readline()
        while linha:
            escrita.write(linha)
            linha = leitura.readline()
