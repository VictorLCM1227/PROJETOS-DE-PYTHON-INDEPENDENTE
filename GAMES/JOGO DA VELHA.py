tabuleiro = [
    ' 1 ', ' 2 ', ' 3 ',
    ' 4 ', ' 5 ', ' 6 ',
    ' 7 ', ' 8 ', ' 9 '
]

jogadorX_texto = 'Jogador X, escolha uma posição: '
jogadorO_texto = 'Jogador O, escolha uma posição: '


def linha():
    print('-' * 42)


def cabeçalho(txt):
    print('=' * 42)
    print(txt.center(42))
    print('=' * 42)


def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar.\033[m')
            return 0
        else:
            return numero


def mostrar_tabuleiro():
    print()
    print(f'{tabuleiro[0]}|{tabuleiro[1]}|{tabuleiro[2]}')
    print('---+---+---')
    print(f'{tabuleiro[3]}|{tabuleiro[4]}|{tabuleiro[5]}')
    print('---+---+---')
    print(f'{tabuleiro[6]}|{tabuleiro[7]}|{tabuleiro[8]}')
    print()


def jogada(jogador, mensagem):
    while True:
        posicao = leiaInt(mensagem) - 1

        if posicao < 0 or posicao > 8:
            print('\033[31mERRO: escolha uma posição entre 1 e 9.\033[m')
            continue

        if 'X' in tabuleiro[posicao] or 'O' in tabuleiro[posicao]:
            print('\033[31mERRO: essa posição já está ocupada.\033[m')
            continue

        tabuleiro[posicao] = f' {jogador} '
        break


def verifica_vitoria(jogador):
    possibilidades = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for possibilidade in possibilidades:
        if (
            jogador in tabuleiro[possibilidade[0]]
            and jogador in tabuleiro[possibilidade[1]]
            and jogador in tabuleiro[possibilidade[2]]
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

    linha()
    mostrar_tabuleiro()

    jogada('X', jogadorX_texto)

    if verifica_vitoria('X'):
        linha()
        mostrar_tabuleiro()
        print('O Jogador X venceu!')
        break

    if verifica_empate():
        linha()
        mostrar_tabuleiro()
        print('Houve um empate!')
        break

    linha()
    mostrar_tabuleiro()

    jogada('O', jogadorO_texto)

    if verifica_vitoria('O'):
        linha()
        mostrar_tabuleiro()
        print('O Jogador O venceu!')
        break

    if verifica_empate():
        linha()
        mostrar_tabuleiro()
        print('Houve um empate!')
        break

print('<< VOLTE SEMPRE >>')