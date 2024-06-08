class ArquivoTXT(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()

    def _extrair_conteudo(self):
        conteudo = None
        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo

    def extrair_linha(self, numero_linha: int):
        return self.conteudo[numero_linha-1]

'''%%writefile noticia.txt
Egito cobra quase US$ 1 bi para liberar navio que bloqueou Canal de Suez
Segundo autoridades, valor será utilizado para recompor as perdas provocados
pelo encalhamento da embarcação de quase 400 metros'''

arquivo_noticia = ArquivoTXT(arquivo='./noticia.txt')

titulo = arquivo_noticia.extrair_linha(numero_linha=1)
print(titulo)


'''
3.2. Definição
Vamos criar um módulo (arquivo) com o nome arquivo_txt.py com o código da
classe ArquivoTXT .
Vamos criar um pacote (pasta) com o nome arquivo e mover os módulos (arquivos)
arquivo_csv.py e arquivo_txt.py para ela.
3.3. Revisitando a motivação
'''

from arquivo.arquivo_csv import ArquivoCSV
from arquivo.arquivo_txt import ArquivoTXT

arquivo_banco_pacote = ArquivoCSV(arquivo='./banco.csv')
arquivo_noticia_pacote = ArquivoTXT(arquivo='./noticia.txt')
education = arquivo_banco_pacote.extrair_coluna(indice_coluna=3)
print(education)

titulo = arquivo_noticia_pacote.extrair_linha(numero_linha=1)
print(titulo)
