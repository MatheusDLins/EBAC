# Um bloco de código que só executado quando chamado.

'''def <nome>(<param 1>, <param 2>, ...):
    bloco de código
    return <valor de retorno>

var = <nome da funcao>(<param 1>, <param 2>, ...)
'''


def imprime(mensagem: str):
    print(mensagem)


texto = 'Fala pessoal, meu nome é André Perez!'

imprime(mensagem='Fala pessoal, meu nome é André Perez!')

# retorno


def maiusculo(texto: str) -> str:
    text_maiusculo = texto.upper()
    return text_maiusculo


def maiusculo(texto: str) -> str:
    text_maiusculo = texto.upper()
    return text_maiusculo


def extrair_usuario_email_provedor(email: str) -> (str, str):
    email_separado = email.split(sep='@')
    usuario = email_separado[0]
    provedor = email_separado[1]
    return usuario, provedor


email = 'andre.perez@gmail.com'
usuario, provedor = extrair_usuario_email_provedor(email=email)
print(usuario)
print(provedor)


def imprime_pi() -> None:
    print(3.14159265359)
    return None


def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:

    try:

        with open(file=nome, mode='w', encoding='utf8') as fp:
            linha = cabecalho + '\n'
            fp.write(linha)
            for conteudo in conteudos:
                linha = str(conteudo) + '\n'
                fp.write(linha)

    except Exception as exc:

        print(exc)
        return False

    return True


nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
# conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]
conteudos = 10

escreveu_com_sucesso = escreve_arquivo_csv(
    nome=nome, cabecalho=cabecalho, conteudos=conteudos)
print(escreveu_com_sucesso)
