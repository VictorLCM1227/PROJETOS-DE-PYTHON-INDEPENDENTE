# blackjack.py

from random import randint

from utilidades import cabeçalho, leiaInt, linha


def blackjack():

    cabeçalho('BLACKJACK 21')

    jogador_pontos = randint(1, 10)

    computador = randint(1, 10)

    while computador < 17:
        computador += randint(1, 10)

    print(f'Seus pontos: {jogador_pontos}')

    while True:

        # Verifica se alguém já ultrapassou 21
        if jogador_pontos > 21:

            print(
                f'Você perdeu com '
                f'{jogador_pontos} pontos.'
            )

            print(
                f'O computador fez '
                f'{computador} pontos.'
            )

            return 'derrota'

        if computador > 21:

            print(
                f'Você venceu! '
                f'O computador passou de 21 '
                f'com {computador} pontos.'
            )

            return 'vitoria'

        # Verifica 21
        if jogador_pontos == 21:

            print(
                'Você fez 21 pontos e venceu!'
            )

            print(
                f'O computador fez '
                f'{computador} pontos.'
            )

            return 'vitoria'

        if computador == 21:

            print(
                'O computador fez 21 pontos '
                'e venceu.'
            )

            return 'derrota'

        print(linha())

        escolha = input(
            'Comprar ou parar? [C/P]: '
        ).strip().upper()

        while escolha not in ('C', 'P'):

            escolha = input(
                'Opção inválida. '
                'Digite C para comprar ou P para parar: '
            ).strip().upper()

        if escolha == 'C':

            carta = randint(1, 10)

            jogador_pontos += carta

            print(
                f'Você tirou {carta}.'
            )

            print(
                f'Seus pontos: '
                f'{jogador_pontos}'
            )

        else:

            if jogador_pontos > computador:

                print(
                    f'Você venceu com '
                    f'{jogador_pontos} pontos!'
                )

                print(
                    f'Computador: '
                    f'{computador} pontos.'
                )

                return 'vitoria'

            elif jogador_pontos < computador:

                print(
                    f'Você perdeu.'
                )

                print(
                    f'Você: {jogador_pontos} | '
                    f'Computador: {computador}'
                )

                return 'derrota'

            else:

                print(
                    f'Empate! Ambos fizeram '
                    f'{jogador_pontos} pontos.'
                )

                return 'empate'