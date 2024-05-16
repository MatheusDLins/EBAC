# Definição
# Armazenam sequências mutáveis e ordenadas de valores. São do tipo `list`:
usuario_web = ['André Perez', 'andre.perez', 'andre123', 'andre.perez@gmail.com']

print(usuario_web)
print(type(usuario_web))

idade = 20
saldo_em_conta = 723.15
usuario_loggedin = True

usuario_web = ['André Perez', idade, 'andre.perez', 'andre123', 'andre.perez@gmail.com', saldo_em_conta, usuario_loggedin]

print(usuario_web)
print(type(usuario_web))

# Operações
# + concatenação
fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua

print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)

# fatiamento
print(f'0: {fabricantes_mobile[0]}')
print(f'-1: {fabricantes_mobile[-1]}')

fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]

print('china: ' + str(fabricantes_mobile_china))
print('eua: ' + str(fabricantes_mobile_eua))

print(fabricantes_mobile)
fabricantes_mobile[2] = 'nokia'
print(fabricantes_mobile)


# Métodos
juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)

# inserir um elemento sem substituir: list.insert(index, val)
juros.insert(0, 0.10)
print(juros)

# inserir um elemento no fim da lista: list.append(val)
juros.append(0.09)
print(juros)

# remover um elemento pelo valor: list.remove(val)
juros.remove(0.1)
print(juros)

# remover um elemento pelo índice: list.pop(val)
terceiro_juros = juros.pop(2)
print(terceiro_juros)

print(juros)


#Conversão
email = 'andre.perez@gmail.com'
caracteres_email = list(email)

print(email)
print(caracteres_email)