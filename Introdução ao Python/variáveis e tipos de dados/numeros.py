#Definição
#Armazenam valores numéricos:

'''
-10, 37, 500(inteiros);
-0.333, 10.1 (decimais);
-1 + 2j (complexos.)

São dos tipos:

-int (inteiros);
-float (decimais);
-complex (complexos).

'''

print(type(37))
print(type(10.1))
print(type(1 + 2j))


#Operações
#As operações dos tipos numéricos são as quatro operações matemáticas fundamentais:
'''
*   `+` (soma);
*   `-` (subtração);
*   `*` (multiplicação);
*   `/` (divisão).

Além de operações mais avançadas:

*   `//` (divisão inteira)
*   `**` (potência ou exponenciação);
*   `%` (resto de divisão).
'''


#Conversão
#Podemos converter os tipos numéricos entre si utilizando o método nativo `int`, `float` e `complex`:

print(int(3.9))
print(float(10))
print(complex(1))