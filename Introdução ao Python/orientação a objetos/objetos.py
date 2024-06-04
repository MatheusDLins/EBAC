from time import sleep


class Pessoa(object):

    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas+1):
            print(f'Dormindo por {hora} horas')
            sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e documento numero {self.documento}'

# Objetos


andre = Pessoa(nome='Andre Duarte', idade=30, documento="123")
beatriz = Pessoa(nome='beatriz Duarte', idade=35, documento="456")
Charles = Pessoa(nome='Charles Duarte', idade=23)


# Atributos
print(andre.nome)


def maior_de_idade(idade: int) -> bool:
    return idade >= 18


if maior_de_idade(idade=andre.idade):
    print(f'{andre.nome} é maior de idade')


score_credito = {'123': 750, '456': 821, '789': 327}

score = score_credito[andre.documento]
print(score)


# Métodos

andre.dormir(horas=8)
andre.falar(texto='olá pessoa!')
print(andre)
type(andre)

# Exemplos
tipos = [
    type(10),
    type(1.1),
    type('EBAC'),
    type(True),
    type(None),
    type([1, 2, 3]),
    type({1, 2, 3}),
    type({'janeiro': 1}),
    type(lambda x: x)
]

for tipo in tipos:
    print(tipo)

nome = 'Andre Perez'
print(nome.upper())

juros = [0.02, 0.07, 0.15]
print(juros.pop(1))


# Classe Arquivo CSV
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

print(arquivo_banco.colunas)

job = arquivo_banco.extrair_coluna(indice_coluna=1)
print(job)

education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)