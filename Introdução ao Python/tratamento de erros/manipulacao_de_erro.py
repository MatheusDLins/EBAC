

# **3.3. Manipulação**
# - Manipular o erro com a estrutura `try-catch-finally-else`.

anos = [2019, 2020, 2021]
anos = {2019, 2020, 2021}

try:
    ano_atual = anos[3]
    print(ano_atual)
except IndexError:
    print('Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))
except Exception as exc:
    print(exc)

#  - Passar o erro para frente com a estrutura `raise`.
anos = [2019, 2020, 2021]
# anos = {2019, 2020, 2021}

try:
    ano_atual = anos[3]
    print(ano_atual)
except IndexError as exc:
    raise Exception(
        'Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))
except Exception as exc:
    raise exc
