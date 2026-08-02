#jokenpo
from time import sleep
from random import randint
from utilidades import leiaInt, continuar_verificacao

def jokenpo(partidas):
        partidas += 1
        itens = ['PEDRA', 'PAPEL', 'TESOURA']
        while True:
            print(f'{" VAMOS JOGAR JOKENPÔ ":=^40}')
            print('''Suas opções:
            [0] para PEDRA
            [1] para PAPEL
            [2] para TESOURA
                ''')
            while True:
                jogador_jogada = leiaInt('Sua jogada? ')
                if 0 <= jogador_jogada <= 2:
                     break
                print('Jogada inválida. Tente novamente!')
            computador = randint(0,2)
            print('JO')
            sleep(0.5)
            print('KEN')
            sleep(0.5)
            print('PÔ!!!')
            print(f'Sua jogada: {itens[jogador_jogada]}')
            print(f'Jogada do computador: {itens[computador]}')
            if jogador_jogada == computador:
                print('EMPATE')
                resultado = 'E'
            elif (jogador_jogada == 0 and computador == 2) or (jogador_jogada == 1 and computador == 0) or (jogador_jogada == 2 and computador == 1):
                    print('VOCÊ GANHOU!')
                    resultado = 'V'
            else:
                print('COMPUTADOR GANHOU!')
                resultado = 'D'
            print('=-=' * 20)
            continuar = continuar_verificacao()
            if continuar == 'N':
                return partidas, resultado