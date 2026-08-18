# adivinhe_o_numero.py

from random import randint

from utilidades import cabeçalho, leiaInt, linha


def adivinhe_o_numero():

    cabeçalho('ADIVINHE O NÚMERO')

    numero = randint(0, 10)
    tentativas = 3

    while tentativas > 0:

        print(f'Tentativas restantes: {tentativas}')

        palpite = leiaInt(
            'Seu palpite (0 a 10): ',
            minimo=0,
            maximo=10
        )

        if palpite == numero:

            print(
                f'\nParabéns! Você acertou!'
            )

            print(
                f'Você precisou de '
                f'{4 - tentativas} tentativa(s).'
            )

            return 'vitoria'

        if palpite < numero:
            print('MAIS...')

        else:
            print('MENOS...')

        tentativas -= 1

        print(linha())

    print(
        f'Você perdeu! '
        f'O número era {numero}.'
    )

    return 'derrota'