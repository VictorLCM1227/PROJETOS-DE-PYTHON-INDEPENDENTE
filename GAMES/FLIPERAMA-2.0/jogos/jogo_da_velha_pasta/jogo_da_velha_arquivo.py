#jogo da velha

from utilidades import linha, leiaInt, cabeçalho
from random import randint

def jogo_da_velha_funcao():

    tabuleiro = [' 1 ', ' 2 ', ' 3 ',  ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
    jogadorX_texto = 'JogadorX Escolha uma posição: '
    jogadorO_texto = 'JogadorO Escolha uma posição: '

    def mostrar_tabuleiro():
        contador = 0
        for linha in range(3):
            for coluna in range(3):
                print(tabuleiro[contador], end='')
                contador += 1
            print()

    def jogadaX():
        while True:
            jogadorX = leiaInt(jogadorX_texto) - 1
            if (0 <= jogadorX <= 8) and (('X' not in tabuleiro[jogadorX]) and ('O' not in tabuleiro[jogadorX])):
                break
            print('Jogada inválida.')
        tabuleiro[jogadorX] = ' X '

    def jogadaO():
        while True:
            jogadorO = randint(0, 8)
            if (0 <= jogadorO <= 8) and (('X' not in tabuleiro[jogadorO]) and ('O' not in tabuleiro[jogadorO])):
                break
        tabuleiro[jogadorO] = ' O '

    def verifica_vitoria():
        if ('X' in tabuleiro[0] and 'X' in tabuleiro[1] and 'X' in tabuleiro[2]) \
        or ('X' in tabuleiro[3] and 'X' in tabuleiro[4] and 'X' in tabuleiro[5]) \
        or ('X' in tabuleiro[6] and 'X' in tabuleiro[7] and 'X' in tabuleiro[8]) \
        or ('X' in tabuleiro[0] and 'X' in tabuleiro[3] and 'X' in tabuleiro[6]) \
        or ('X' in tabuleiro[1] and 'X' in tabuleiro[3] and 'X' in tabuleiro[7]) \
        or ('X' in tabuleiro[2] and 'X' in tabuleiro[5] and 'X' in tabuleiro[8]) \
        or ('X' in tabuleiro[0] and 'X' in tabuleiro[4] and 'X' in tabuleiro[8]) \
        or ('X' in tabuleiro[2] and 'X' in tabuleiro[4] and 'X' in tabuleiro[6]):
            return True
        elif ('O' in tabuleiro[0] and 'O' in tabuleiro[1] and 'O' in tabuleiro[2]) \
        or ('O' in tabuleiro[3] and 'O' in tabuleiro[4] and 'O' in tabuleiro[5]) \
        or ('O' in tabuleiro[6] and 'O' in tabuleiro[7] and 'O' in tabuleiro[8]) \
        or ('O' in tabuleiro[0] and 'O' in tabuleiro[3] and 'O' in tabuleiro[6]) \
        or ('O' in tabuleiro[1] and 'O' in tabuleiro[3] and 'O' in tabuleiro[7]) \
        or ('O' in tabuleiro[2] and 'O' in tabuleiro[5] and 'O' in tabuleiro[8]) \
        or ('O' in tabuleiro[0] and 'O' in tabuleiro[4] and 'O' in tabuleiro[8]) \
        or ('O' in tabuleiro[2] and 'O' in tabuleiro[4] and 'O' in tabuleiro[6]):
            return True


    def verifica_empate():
        if not verifica_vitoria():
            contador = 0
            for item in tabuleiro:
                if 'X' in item or 'O' in item:
                    contador += 1
            if contador == 9:
                return True


    cabeçalho('JOGO DA VELHA')
    while True:
        print(linha())
        mostrar_tabuleiro()
        print(linha())
        jogadaX()
        print(linha())
        mostrar_tabuleiro()
        if verifica_vitoria():
            print('Você venceu!')
            return 'V'
        if verifica_empate():
            print('Houve um empate!')
            return 'E'
        print(linha())
        jogadaO()
        print(linha())
        mostrar_tabuleiro()
        if verifica_vitoria():
            print('Você perdeu!')
            return 'D'
        if verifica_empate():
            print('Houve um empate!')
            return 'E'