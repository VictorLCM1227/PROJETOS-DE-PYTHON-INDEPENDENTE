# utilidades.py

from time import sleep


def linha(tamanho=50):
    print('-' * tamanho)


def cabeçalho(titulo, tamanho=50):
    linha(tamanho)
    print(titulo.center(tamanho))
    linha(tamanho)


def pausa():
    input('\nPressione ENTER para continuar...')


def limpar_tela():
    # Se você já possui uma implementação para isso,
    # mantenha-a aqui.
    ...


def menu(opcoes, titulo='MENU'):
    cabeçalho(titulo)

    for numero, opcao in enumerate(opcoes):
        print(f'{numero} - {opcao}')

    while True:
        try:
            escolha = int(input('Escolha uma opção: '))

            if 0 <= escolha < len(opcoes):
                return escolha

            print('ERRO: opção inválida.')

        except ValueError:
            print('ERRO: digite um número válido.')


def leia_int(msg, minimo=None, maximo=None):

    while True:
        try:
            numero = int(input(msg))

            if minimo is not None and numero < minimo:
                print(f'ERRO: digite um valor maior ou igual a {minimo}.')
                continue

            if maximo is not None and numero > maximo:
                print(f'ERRO: digite um valor menor ou igual a {maximo}.')
                continue

            return numero

        except ValueError:
            print('ERRO: digite um número inteiro válido.')


def leia_float(msg, minimo=None, maximo=None):

    while True:
        try:
            numero = float(input(msg))

            if minimo is not None and numero < minimo:
                print(f'ERRO: digite um valor maior ou igual a {minimo}.')
                continue

            if maximo is not None and numero > maximo:
                print(f'ERRO: digite um valor menor ou igual a {maximo}.')
                continue

            return numero

        except ValueError:
            print('ERRO: digite um número válido.')


def esperar(segundos=1):
    sleep(segundos)