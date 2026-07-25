tabuleiro = [' 1 ', ' 2 ', ' 3 ',  ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
jogadorX_texto = 'JogadorX Escolha uma posição: '
jogadorO_texto = 'JogadorO Escolha uma posição: '

def linha():
    print('-' * 42)

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número interiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

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
        jogadorO = leiaInt(jogadorO_texto) - 1
        if (0 <= jogadorO <= 8) and (('X' not in tabuleiro[jogadorO]) and ('O' not in tabuleiro[jogadorO])):
            break
        print('Jogada inválida.')
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


def cabeçalho(txt):
    print('=' * 42)
    print(txt.center(42))
    print('=' * 42)

cabeçalho('JOGO DA VELHA')
while True:
    linha()
    mostrar_tabuleiro()
    jogadaX()
    linha()
    mostrar_tabuleiro()
    if verifica_vitoria():
        print('O Jogador X venceu!')
        break
    if verifica_empate():
        print('Houve um empate!')
        break
    jogadaO()
    linha()
    mostrar_tabuleiro()
    if verifica_vitoria():
        print('O jogador O venceu!')
        break
    if verifica_empate():
        print('Houve um empate!')
        break
print('<< VOLTE SEMPRE >>')