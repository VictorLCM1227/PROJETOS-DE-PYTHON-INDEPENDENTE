#menu principal
from perfil import mostrar_perfil
from carteira import depositar, sacar, mostrar_extrato, validar_aposta, atualizar_aposta
from utilidades import leiaInt, linha, cabeçalho, menu
from jogador import ficha_do_jogador
from jogos import jokenpo, par_ou_impar


print('BEM VINDO!!!')




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
                aposta = validar_aposta(ficha_do_jogador['saldo'])
                if aposta is None:
                    print('Por isso não foi possível apostar.')
                else:
                    ficha_do_jogador['saldo'] -= aposta
                    ficha_do_jogador['extrato'].append(('Aposta Jokenpô', -aposta))
                    ficha_do_jogador['partidas'], resultado = jokenpo.jokenpo(ficha_do_jogador['partidas'])
                    atualizar_aposta(ficha_do_jogador, aposta, resultado)


            elif escolha_jogo == 2:
                cabeçalho('PAR OU ÍMPAR')
                aposta = validar_aposta(ficha_do_jogador['saldo'])
                if aposta is None:
                    print('Por isso não foi possível apostar.')
                else:
                    ficha_do_jogador['saldo'] -= aposta
                    ficha_do_jogador['extrato'].append(('Aposta Par ou Ímpar', -aposta))
                    ficha_do_jogador['partidas'], resultado = par_ou_impar.par_ou_impar(ficha_do_jogador['partidas'])
                    atualizar_aposta(ficha_do_jogador, aposta, resultado)

                

            elif escolha_jogo == 3:
                cabeçalho('ADIVINHE O NÚMERO')
                

    elif escolha_principal == 2:
        mostrar_perfil(nome=ficha_do_jogador['nome'], saldo=ficha_do_jogador['saldo'], jogos_jogados=ficha_do_jogador['partidas'])

    elif escolha_principal == 3:
        cabeçalho('CARTEIRA')
        print(f'Saldo atual: R${ficha_do_jogador["saldo"]} ')
        escolha_carteira = menu(lista=['VOLTAR', 'DEPOSITAR', 'SACAR', 'EXTRATO'], menu_titulo='')
        if escolha_carteira == 0:
            cabeçalho('VOLTANDO')

        elif escolha_carteira == 1:
            cabeçalho('DEPOSITAR')
            ficha_do_jogador['saldo'], ficha_do_jogador['extrato'] = depositar(ficha_do_jogador['saldo'], ficha_do_jogador['extrato'])

        elif escolha_carteira == 2:
            cabeçalho('SACAR')
            ficha_do_jogador['saldo'], ficha_do_jogador['extrato'] = sacar(ficha_do_jogador['saldo'], ficha_do_jogador['extrato'])

        elif escolha_carteira == 3:
            cabeçalho('EXTRATO')
            mostrar_extrato(ficha_do_jogador['extrato'])


