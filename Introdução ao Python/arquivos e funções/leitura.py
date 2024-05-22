# Comando para ler arquivos.

'''
with open(file='<caminho do arquivo>', mode='<modo de leitura>', encoding='<decodificador>') as <apelido>:
    bloco de código
'''

conteudo = None

with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()

#Os modos de leitura são: r: Abrir o arquivo para leitura (padrão).

#print(conteudo)


# readline
# Comando para ler o conteúdo de um arquivo uma linha por vez.

conteudo = []

with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        conteudo.append(linha)
        # lê uma nova linha, se a linha não existir salva o valor None
        linha = arquivo.readline()

print(conteudo[8])

'''for linha in conteudo:
    print(linha)'''


# Exemplo: Extraindo os valores da primeira coluna (idade).
idades = []

with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        # quebra a string nas virgulas(ponto e virgula) e salva os resultados em uma lista
        linha_separada = linha.split(sep=';')
        idade = linha_separada[0]  # seleciona o primeiro elemento da lista
        idade = str(idade)  # converte o valor de string para integer (inteiro)
        idades.append(idade)  # salva o valor na lista de idades
        # lê uma nova linha, se a linha não existir, salva o valor None
        linha = arquivo.readline()


#print(idades)
