from arquivo_csv import ArquivoCSV


class ArquivoCSV(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()
        self.colunas = self._extrair_nome_colunas()
        
    def _extrair_conteudo(self):
        conteudo = None
        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo

    def _extrair_nome_colunas(self):
        return self.conteudo[0].strip().split(sep=',')

    def extrair_coluna(self, indice_coluna: str):
        coluna = list()
        for linha in self.conteudo:
            conteudo_linha = linha.strip().split(sep=',')
            coluna.append(conteudo_linha[indice_coluna])
        coluna.pop(0)
        return coluna

# Arquivo banco.csv


'''%%writefile banco.csv
age,job,marital,education,default,balance,housing,loan
30,unemployed,married,primary,no,1787,no,no
33,services,married,secondary,no,4789,yes,yes
35,management,single,tertiary,no,1350,yes,no
30,management,married,tertiary,no,1476,yes,yes
59,blue-collar,married,secondary,no,0,yes,no
35,management,single,tertiary,no,747,no,no
36,self-employed,married,tertiary,no,307,yes,no
39,technician,married,secondary,no,147,yes,no
41,entrepreneur,married,tertiary,no,221,yes,no
43,services,married,primary,no,-88,yes,yes'''


arquivo_banco = ArquivoCSV(arquivo='./banco.csv')

# Extraindo a coluna de education

education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)

'''
2.2. Definição
Vamos criar um módulo (arquivo) com o nome arquivo_csv.py com o código da classe
ArquivoCSV .
2.3. Revisitando a motivação
Vamos importar a classe ArquivoCSV do módulo (arquivo) arquivo_csv.py .
'''

arquivo_banco_modulo = ArquivoCSV(arquivo='./banco.csv')
education = arquivo_banco_modulo.extrair_coluna(indice_coluna=3)
print(education)
