'''
%%writefile carros.csv
id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
1,vhigh,med,2,2,small
2,med,vhigh,2,2,small
3,low,vhigh,2,2,small
4,low,high,2,2,small
5,low,high,2,2,small
6,low,high,4,4,big
7,low,high,4,4,big
8,low,med,2,2,small
9,low,med,2,2,small
10,low,med,2,2,small
11,low,med,4,4,big
12,low,low,2,2,small
13,low,low,4,4,small
14,low,low,4,4,med


%%writefile musica.txt
Roda Viva
Chico Buarque

Tem dias que a gente se sente
Como quem partiu ou morreu
A gente estancou de repente
Ou foi o mundo então que cresceu
A gente quer ter voz ativa
No nosso destino mandar
Mas eis que chega a roda viva
E carrega o destino pra lá

Roda mundo, roda-gigante
Roda moinho, roda pião

O tempo rodou num instante
Nas voltas do meu coração
A gente vai contra a corrente
Até não poder resistir
Na volta do barco é que sente
O quanto deixou de cumprir
Faz tempo que a gente cultiva
A mais linda roseira que há
Mas eis que chega a roda viva
E carrega a roseira pra lá

Roda mundo, roda-gigante
Roda moinho, roda pião


1. Classe para ler arquivos de texto
Crie a classe ArquivoTexto. Ela deve conter os seguintes atributos:

self.arquivo: Atributo do tipo str com o nome do arquivo;
self.conteudo: Atributo do tipo list onde cada elemento é uma linha do arquivo;
A classe também deve conter o seguinte método:

self.extrair_linha: Método que recebe como parâmetro o número da linha e retorna o seu conteúdo.
'''


class ArquivoTexto(object):

    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = []

        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            linha = arquivo.readline()  # lê a primeira linha
            while linha:
                self.conteudo.append(linha)
                # lê uma nova linha, se a linha não existir salva o valor None
                linha = arquivo.readline()

    def extrair_linha(self, numero_linha: int):
        return (self.conteudo[numero_linha - 1])


# Utilize o código abaixo para testar sua classe.
arquivo_texto = ArquivoTexto(arquivo='musica.txt')

numero_linha = 1
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))  # Roda Viva

numero_linha = 10
# Mas eis que chega a roda viva
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))


'''
2. Classe para ler arquivos de csv
Crie a classe ArquivoCSV. Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos (self.arquivo e self.conteudo) e método (self.extrair_linha). Além disso, adicione o seguinte atributo:

self.colunas: Atributo do tipo list onde os elementos são os nome das colunas;
A classe também deve conter o seguinte método:

self.extrair_coluna_da_linha: Método que recebe como parâmetro o numero da linha e o indice da coluna e retorna o valor em questão.
'''


class ArquivoCSV(ArquivoTexto):

    def __init__(self, arquivo: str):

        super().__init__(arquivo=arquivo)
        self.colunas = self.conteudo[0].split(',')

    def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):
        return (self.conteudo[numero_linha - 1].split(',')[numero_coluna - 1])

# Utilize o código abaixo para testar sua classe.


arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 1
# id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

# ['id', 'valor_venda', 'valor_manutencao', 'portas', 'pessoas', 'porta_malas']
print(arquivo_csv.colunas)

numero_linha = 10
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))  # 9,low,med,2,2,small

numero_linha = 10
numero_coluna = 2
print(arquivo_csv.extrair_coluna_da_linha(
    numero_linha=numero_linha, numero_coluna=numero_coluna))  # low
