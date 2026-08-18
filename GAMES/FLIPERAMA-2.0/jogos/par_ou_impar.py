# par_ou_impar.py

from random import randint
from time import sleep

from utilidades import cabeçalho, leiaInt


def par_ou_impar():

    cabeçalho('PAR OU ÍMPAR')

    while True:

        opcao = input(
            'ÍMPAR ou PAR? [I/P]: '
        ).strip().upper()

        if opcao in ('I', 'P'):
            break

        print(
            'Opção inválida! '
            'Escolha I ou P.'
        )

    jogador = leiaInt(
        'Escolha um número: '
    )

    computador = randint(0, 10)

    print('\nÍMPAR')
    sleep(0.5)

    print('OU')
    sleep(0.5)

    print('PAR!!!')

    soma = jogador + computador

    print(
        f'\nJogador: {jogador}'
    )

    print(
        f'Computador: {computador}'
    )

    print(
        f'Soma: {jogador} + {computador} = {soma}'
    )

    resultado = 'P' if soma % 2 == 0 else 'I'

    print(
        f'Resultado: '
        f'{"PAR" if resultado == "P" else "ÍMPAR"}'
    )

    if opcao == resultado:

        print('VOCÊ VENCEU!')

        return 'vitoria'

    print('COMPUTADOR VENCEU!')

    return 'derrota'