#dados
from random import randint
from time import sleep
from utilidades import leiaIntPositivo

def jogo_de_dados():
    lados = leiaIntPositivo('Quantos lados gostaria no dado? O minimo é um dado de 6 lados.  ')
    if lados < 6:
        lados = 6
    print(f'Você escolheu um dado de {lados} lados.')
    dado = randint(1, lados)
    print('O dado foi jogado...')
    while True:
        jogador = leiaIntPositivo('Em qual lado você acha que caiu? ')
        if jogador <= lados:
            break
        print('Escolha um lado existente por favor.')
    sleep(1)
    print(f'O dado caiu no lado {dado}.')
    if jogador == dado:
        print('VOCÊ GANHOU!')
        return 'V'
    else:
        print('COMPUTADOR GANHOU!')
        return 'D'