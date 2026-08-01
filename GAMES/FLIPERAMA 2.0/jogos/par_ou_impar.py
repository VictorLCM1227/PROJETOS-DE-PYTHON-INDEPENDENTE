#par ou impar

from time import sleep
from utilidades import leiaInt, continuar_verificacao
from random import randint

def par_ou_impar():
    while True:
        print(f'{" IMPAR OU PAR ":=^40}')
        while True:
            try:
                opcao = input('ÍMPAR ou PAR? [P/I] ').upper().strip()[0]
            except:
                print('ERRO! Por favor escolha P ou I.')
            else:
                if opcao in 'PI':
                    break
        jogador_numero = leiaInt('Escolha um número: ')
        print('IMPAR')
        sleep(0.5)
        print('OU')
        sleep(0.5)
        print('PAR!!!')
        pc = randint(0, 10)
        soma = jogador_numero + pc
        if opcao == 'I':
            print('JOGADOR Escolheu IMPAR e COMPUTADOR escolheu PAR')
        else:
            print('JOGADOR escolheu PAR e COMPUTADOR escolheu IMPAR')
        print(f' Você {jogador_numero} + computador {pc} = {soma}')
        if soma % 2 == 0:
            resultado = 'P'
        else:
            resultado = 'I'
        if opcao == resultado:
            print('JOGADOR VENCEU')
        else:
            print('COMPUTADOR VENCEU')
        print('-=-'*20)
        continuar = continuar_verificacao()
        if continuar == 'N':
            break