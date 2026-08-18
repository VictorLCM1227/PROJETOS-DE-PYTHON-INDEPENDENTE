# dados.py

from random import randint
from time import sleep

from utilidades import cabeçalho, leiaIntPositivo


def jogo_de_dados():

    cabeçalho('JOGO DE DADOS')

    while True:

        lados = leiaIntPositivo(
            'Quantos lados terá o dado? '
            '(mínimo 6): '
        )

        if lados >= 6:
            break

        print(
            'O dado precisa ter pelo menos '
            '6 lados.'
        )

    print(
        f'\nVocê escolheu um dado de '
        f'{lados} lados.'
    )

    dado = randint(1, lados)

    print('O dado foi jogado...')

    while True:

        palpite = leiaIntPositivo(
            'Em qual lado você acha que caiu? '
        )

        if palpite <= lados:
            break

        print(
            f'Escolha um número entre '
            f'1 e {lados}.'
        )

    sleep(1)

    print(
        f'\nO dado caiu no lado {dado}.'
    )

    if palpite == dado:

        print('VOCÊ GANHOU!')

        return 'vitoria'

    print('VOCÊ PERDEU!')

    return 'derrota'