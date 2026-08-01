##menu principal
from perfil import mostrar_perfil
from carteira import mostrar_saldo
from utilidades import leiaInt, linha, cabeçalho, menu
saldo = 0
jogos_jogados = 0


print('BEM VINDO!!!')
nome = input('Qual o seu nome? ').strip()

while True:
    escolha_principal = menu(lista=['SAIR', 'JOGAR', 'PERFIL', 'CARTEIRA'], menu_titulo='FLIPERAMA DO VICTOR')

    if escolha_principal == 0:
        cabeçalho('SAINDO')
        break

    elif escolha_principal == 1:
        cabeçalho('JOGAR')
        while True:
            escolha_jogo = menu(lista=['VOLTAR', 'JOKENPÔ', 'PAR OU ÍMPAR', 'ADIVINHE O NÚMERO'], menu_titulo='JOGOS')

            if escolha_jogo == 0:
                cabeçalho('VOLTANDO')
                break

            elif escolha_jogo == 1:
                cabeçalho('JOKENPÔ')

            elif escolha_jogo == 2:
                cabeçalho('PAR OU ÍMPAR')

            elif escolha_jogo == 3:
                cabeçalho('ADIVINHE O NÚMERO')

    elif escolha_principal == 2:
        mostrar_perfil(nome=nome, saldo=saldo, jogos_jogados=jogos_jogados)

    elif escolha_principal == 3:
        mostrar_saldo(saldo=saldo)


