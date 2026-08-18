from time import sleep

historico = []


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


def pausa():
    sleep(1)


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


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero

        except ValueError:
            print('\033[31mERRO: digite um número real válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mOperação cancelada pelo usuário.\033[m')
            return 0


def pegar_numeros(msg1, msg2):
    numero1 = leiaFloat(msg1)
    numero2 = leiaFloat(msg2)

    return numero1, numero2


# ==============================
# FUNÇÕES DO HISTÓRICO
# ==============================

def adicionar_historico(resultado):
    historico.append(resultado)
    print(f'\n\033[32m{resultado}\033[m')


def mostrar_historico():
    cabecalho('HISTÓRICO')

    if not historico:
        print('Nenhuma operação foi realizada.')
    else:
        for contador, operacao in enumerate(historico, start=1):
            print(f'\033[33m[{contador}]\033[m - \033[34m{operacao}\033[m')

    print(linha())


def limpar_historico():
    cabecalho('LIMPAR HISTÓRICO')

    if not historico:
        print('O histórico já está vazio.')
    else:
        historico.clear()
        print('\033[32mHistórico apagado com sucesso!\033[m')


# ==============================
# OPERAÇÕES
# ==============================

def somar():
    cabecalho('SOMAR')

    numero1, numero2 = pegar_numeros(
        'Digite o primeiro número: ',
        'Digite o segundo número: '
    )

    resultado = numero1 + numero2

    adicionar_historico(
        f'{numero1} + {numero2} = {resultado}'
    )


def subtrair():
    cabecalho('SUBTRAIR')

    numero1, numero2 = pegar_numeros(
        'Digite o primeiro número: ',
        'Digite o segundo número: '
    )

    resultado = numero1 - numero2

    adicionar_historico(
        f'{numero1} - {numero2} = {resultado}'
    )


def multiplicar():
    cabecalho('MULTIPLICAR')

    numero1, numero2 = pegar_numeros(
        'Digite o primeiro número: ',
        'Digite o segundo número: '
    )

    resultado = numero1 * numero2

    adicionar_historico(
        f'{numero1} × {numero2} = {resultado}'
    )


def dividir():
    cabecalho('DIVIDIR')

    numero1, numero2 = pegar_numeros(
        'Digite o dividendo: ',
        'Digite o divisor: '
    )

    if numero2 == 0:
        print('\033[31mERRO: não é possível dividir por zero.\033[m')
        return

    resultado = numero1 / numero2

    adicionar_historico(
        f'{numero1} ÷ {numero2} = {resultado:.2f}'
    )


def potencia():
    cabecalho('POTÊNCIA')

    base, expoente = pegar_numeros(
        'Digite a base: ',
        'Digite o expoente: '
    )

    resultado = base ** expoente

    adicionar_historico(
        f'{base} ^ {expoente} = {resultado}'
    )


def raiz():
    cabecalho('RAIZ')

    while True:
        radicando = leiaFloat('Digite o radicando: ')

        if radicando >= 0:
            break

        print('\033[31mERRO: o radicando deve ser maior ou igual a zero.\033[m')

    while True:
        indice = leiaFloat('Digite o índice da raiz: ')

        if indice > 0:
            break

        print('\033[31mERRO: o índice deve ser maior que zero.\033[m')

    resultado = radicando ** (1 / indice)

    adicionar_historico(
        f'Raiz {indice} de {radicando} = {resultado:.2f}'
    )


def resto_divisao():
    cabecalho('RESTO DA DIVISÃO')

    dividendo, divisor = pegar_numeros(
        'Digite o dividendo: ',
        'Digite o divisor: '
    )

    if divisor == 0:
        print('\033[31mERRO: não é possível dividir por zero.\033[m')
        return

    resultado = dividendo % divisor

    adicionar_historico(
        f'{dividendo} % {divisor} = {resultado}'
    )


def divisao_inteira():
    cabecalho('DIVISÃO INTEIRA')

    dividendo, divisor = pegar_numeros(
        'Digite o dividendo: ',
        'Digite o divisor: '
    )

    if divisor == 0:
        print('\033[31mERRO: não é possível dividir por zero.\033[m')
        return

    resultado = dividendo // divisor

    adicionar_historico(
        f'{dividendo} // {divisor} = {resultado}'
    )


# ==============================
# MENU
# ==============================

def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for numero, item in enumerate(lista):
        print(f'\033[33m[{numero}]\033[m - \033[34m{item}\033[m')

    print(linha())

    return leiaInt('\033[32mSua opção: \033[m')


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

opcoes = [
    'Sair',
    'Somar',
    'Subtrair',
    'Multiplicar',
    'Dividir',
    'Potência',
    'Raiz',
    'Resto da divisão',
    'Divisão inteira',
    'Histórico',
    'Limpar histórico'
]


operacoes = {
    1: somar,
    2: subtrair,
    3: multiplicar,
    4: dividir,
    5: potencia,
    6: raiz,
    7: resto_divisao,
    8: divisao_inteira,
    9: mostrar_historico,
    10: limpar_historico
}


cabecalho('CALCULADORA')

while True:

    opcao = menu(opcoes)

    if opcao == 0:
        cabecalho('Saindo do sistema... Até logo!')
        break

    if opcao in operacoes:
        operacoes[opcao]()
    else:
        cabecalho('ERRO')
        print('\033[31mDigite uma opção válida!\033[m')

    pausa()