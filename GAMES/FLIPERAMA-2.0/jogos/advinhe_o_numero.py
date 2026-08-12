#advinhe o número
from random import randint

def adivinhe_o_numero():
    print(f'{" ADIVINHE O NÚMERO (0 a 10)":=^40}')
    tentativas = 3
    computador = randint(0, 10)
    while True:
        print(f'Tentativas: {tentativas}')
        jogador_palpite = int(input('Seu palpite: '))
        while jogador_palpite > 10 or jogador_palpite < 0:
            jogador_palpite = int(input('Palpite inválido. Tente novamente! Seu palpite: '))
        if jogador_palpite == computador:
            print('Parabéns! Você acertou!')
            print(f'E precisou de {tentativas} tentativas.')
            return 'V'
        elif jogador_palpite < computador:
            print('MAIS...')
        elif jogador_palpite > computador:
            print('MENOS...')
        tentativas -= 1
        print('-'*40)
        if tentativas == 0:
            print(f'Você não conseguiu acertar, o número era {computador}')
            return 'D'