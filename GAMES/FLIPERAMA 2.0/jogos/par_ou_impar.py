#par ou impar

from time import sleep
from utilidades import leiaInt, continuar_verificacao
from random import randint

def par_ou_impar(partidas):
    partidas += 1
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
        return partidas, resultado

'''
1. Corrigir inconsistências (prioridade máxima)

Há alguns pontos que ainda estão usando a estrutura antiga.

No perfil

Você faz:

ficha_do_jogador['vitoria']

e

ficha_do_jogador['partidas']

Mas sua ficha agora possui:

vitorias_totais
partidas_totais

Além disso, antes de calcular a taxa de vitória, trate o caso em que o jogador ainda não jogou nenhuma partida, para evitar divisão por zero.

No Par ou Ímpar

Seu jokenpo() devolve:

'V'
'D'
'E'

Já o par_ou_impar() devolve:

'P'
'I'

Só que atualizar_aposta() entende apenas:

'V'
'D'
'E'

Então o próximo passo é fazer o Par ou Ímpar retornar exatamente o mesmo padrão.
'''