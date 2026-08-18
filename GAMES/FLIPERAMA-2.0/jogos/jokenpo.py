# jokenpo.py

from random import randint
from time import sleep

from utilidades import cabeçalho, leiaInt


def jokenpo():

    itens = [
        'PEDRA',
        'PAPEL',
        'TESOURA'
    ]

    cabeçalho('JOKENPÔ')

    print(
        '[0] PEDRA\n'
        '[1] PAPEL\n'
        '[2] TESOURA'
    )

    while True:

        jogador = leiaInt(
            'Sua jogada: '
        )

        if 0 <= jogador <= 2:
            break

        print(
            'Jogada inválida. '
            'Escolha 0, 1 ou 2.'
        )

    computador = randint(0, 2)

    print('\nJO')
    sleep(0.5)

    print('KEN')
    sleep(0.5)

    print('PÔ!!!')

    print(
        f'\nSua jogada: '
        f'{itens[jogador]}'
    )

    print(
        f'Jogada do computador: '
        f'{itens[computador]}'
    )

    if jogador == computador:

        print('EMPATE!')

        return 'empate'

    # Pedra vence Tesoura
    # Papel vence Pedra
    # Tesoura vence Papel

    jogador_venceu = (
        (jogador == 0 and computador == 2)
        or
        (jogador == 1 and computador == 0)
        or
        (jogador == 2 and computador == 1)
    )

    if jogador_venceu:

        print('VOCÊ GANHOU!')

        return 'vitoria'

    print('COMPUTADOR GANHOU!')

    return 'derrota'