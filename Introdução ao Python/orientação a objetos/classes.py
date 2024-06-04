#Classes
#Definição
'''
class NomeClasse(object):

    def __init__(self, params):
        self.atributo1 = ...
        self.atributo2 = ...

    def metodo1(self, params):
        ...

    def metodo2(self, params):
        ...
'''

'''class Pessoa(object):

    def __init__(self):
        pass

#Atributos

class Pessoa(object):

    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self.idade = idade
        self.documento = documento'''

from time import sleep

class Pessoa(object):

    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas+1):
            print(f'Dormindo por {hora} horas')
            sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__ (self) -> str:
        return f'{self.nome}, {self.idade} anos e documento numero {self.documento}'

