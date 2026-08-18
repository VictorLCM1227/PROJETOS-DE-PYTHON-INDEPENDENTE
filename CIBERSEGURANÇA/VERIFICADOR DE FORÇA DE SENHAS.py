from time import sleep


# ==============================
# INTERFACE
# ==============================

def linha(simbolo='-', tam=50):
    return simbolo * tam


def cabecalho(txt, simbolo='-'):
    print(linha(simbolo))
    print(txt.center(50))
    print(linha(simbolo))


# ==============================
# VERIFICAÇÕES
# ==============================

def verificar_tamanho(senha):
    print('Possui 8 ou mais caracteres: ', end='')

    if len(senha) >= 8:
        print('SIM')
        return 1

    print('NÃO')
    return 0


def verificar_maiuscula(senha):
    print('Possui letras maiúsculas: ', end='')

    for letra in senha:
        if letra.isupper():
            print('SIM')
            return 1

    print('NÃO')
    return 0


def verificar_minuscula(senha):
    print('Possui letras minúsculas: ', end='')

    for letra in senha:
        if letra.islower():
            print('SIM')
            return 1

    print('NÃO')
    return 0


def verificar_numero(senha):
    print('Possui números: ', end='')

    for letra in senha:
        if letra.isnumeric():
            print('SIM')
            return 1

    print('NÃO')
    return 0


def verificar_especial(senha):
    print('Possui caracteres especiais: ', end='')

    for letra in senha:
        if not letra.isalnum():
            print('SIM')
            return 1

    print('NÃO')
    return 0


# ==============================
# CÁLCULO DA FORÇA
# ==============================

def calcular_forca(pontos):
    if pontos == 5:
        nivel = 'FORTE'

    elif pontos >= 3:
        nivel = 'MÉDIA'

    else:
        nivel = 'FRACA'

    print(f'\nSenha {nivel}')


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

cabecalho('VERIFICADOR DE SENHA', simbolo='=')

senha = input('Digite sua senha: ')

print('\nAnalisando...')
sleep(0.5)

pontos = 0

pontos += verificar_tamanho(senha)
pontos += verificar_maiuscula(senha)
pontos += verificar_minuscula(senha)
pontos += verificar_numero(senha)
pontos += verificar_especial(senha)

print()
print(f'Pontuação: {pontos}/5')

calcular_forca(pontos)