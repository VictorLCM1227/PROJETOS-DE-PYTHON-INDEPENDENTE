# jogo_da_velha.py

from random import randint

from utilidades import linha, leiaInt, cabeçalho


def jogo_da_velha():

    tabuleiro = [
        ' 1 ', ' 2 ', ' 3 ',
        ' 4 ', ' 5 ', ' 6 ',
        ' 7 ', ' 8 ', ' 9 '
    ]

    def mostrar_tabuleiro():

        contador = 0

        for _ in range(3):

            for _ in range(3):
                print(tabuleiro[contador], end='')
                contador += 1

            print()

    def jogada_jogador():

        while True:

            posicao = leiaInt(
                'Jogador X escolha uma posição: '
            ) - 1

            if not 0 <= posicao <= 8:
                print('Jogada inválida.')
                continue

            if (
                'X' in tabuleiro[posicao]
                or 'O' in tabuleiro[posicao]
            ):
                print('Essa posição já está ocupada.')
                continue

            tabuleiro[posicao] = ' X '
            break

    def jogada_computador():

        while True:

            posicao = randint(0, 8)

            if (
                'X' not in tabuleiro[posicao]
                and 'O' not in tabuleiro[posicao]
            ):
                tabuleiro[posicao] = ' O '
                break

    def verifica_vitoria(jogador):

        combinacoes = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in combinacoes:

            if (
                jogador in tabuleiro[a]
                and jogador in tabuleiro[b]
                and jogador in tabuleiro[c]
            ):
                return True

        return False

    def verifica_empate():

        for posicao in tabuleiro:

            if 'X' not in posicao and 'O' not in posicao:
                return False

        return True

    cabeçalho('JOGO DA VELHA')

    while True:

        print(linha())
        mostrar_tabuleiro()
        print(linha())

        # Jogador
        jogada_jogador()

        print(linha())
        mostrar_tabuleiro()

        if verifica_vitoria('X'):
            print('Você venceu!')
            return 'vitoria'

        if verifica_empate():
            print('Houve um empate!')
            return 'empate'

        # Computador
        print(linha())
        jogada_computador()

        print(linha())
        mostrar_tabuleiro()

        if verifica_vitoria('O'):
            print('Você perdeu!')
            return 'derrota'

        if verifica_empate():
            print('Houve um empate!')
            return 'empate'