# ==============================
# FUNÇÕES DE ENTRADA
# ==============================

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except ValueError:
            print('\033[31mERRO: digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mOperação cancelada pelo usuário.\033[m')
            return 0


# ==============================
# FUNÇÕES DE INTERFACE
# ==============================

def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print()
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for indice, item in enumerate(lista):
        print(f'\033[33m[{indice}]\033[m - \033[34m{item}\033[m')

    print(linha())

    return leiaInt('\033[32mSua opção: \033[m')


# ==============================
# CRIPTOGRAFIA
# ==============================

def criptografar(texto, chave):
    texto_numeros = []

    for letra in texto:
        numero = ord(letra) + chave
        texto_numeros.append(numero)

    texto_criptografado = []

    for numero in texto_numeros:
        texto_criptografado.append(chr(numero))

    return ''.join(texto_criptografado)


def descriptografar(texto, chave):
    texto_numeros = []

    for letra in texto:
        numero = ord(letra) - chave
        texto_numeros.append(numero)

    texto_descriptografado = []

    for numero in texto_numeros:
        texto_descriptografado.append(chr(numero))

    return ''.join(texto_descriptografado)


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

opcoes = [
    'Sair',
    'Criptografar',
    'Descriptografar'
]


while True:

    opcao = menu(opcoes)

    if opcao == 0:
        cabecalho('SAINDO DO SISTEMA...')
        print('Até logo!')
        break

    elif opcao == 1:
        cabecalho('CRIPTOGRAFAR')

        texto = input(
            'Digite a mensagem a ser criptografada: '
        )

        chave = leiaInt(
            'Digite a chave da criptografia: '
        )

        resultado = criptografar(texto, chave)

        print(f'\nMensagem criptografada:')
        print(f'\033[32m{resultado}\033[m')

    elif opcao == 2:
        cabecalho('DESCRIPTOGRAFAR')

        texto = input(
            'Digite a mensagem a ser descriptografada: '
        )

        chave = leiaInt(
            'Digite a chave da criptografia: '
        )

        resultado = descriptografar(texto, chave)

        print(f'\nMensagem descriptografada:')
        print(f'\033[32m{resultado}\033[m')

    else:
        cabecalho('ERRO')
        print('\033[31mDigite uma opção válida!\033[m')