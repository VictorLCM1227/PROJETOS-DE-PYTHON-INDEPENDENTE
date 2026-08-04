#menu principal
from perfil import mostrar_perfil
from carteira import depositar, sacar, mostrar_extrato, validar_aposta, atualizar_aposta
from utilidades import leiaInt, linha, cabeçalho, menu
from jogador import ficha_do_jogador
from jogos import jokenpo, par_ou_impar

def gerencia_partidas(jogo_nome, jogo, jogo_estatisticas):
    cabeçalho(jogo_nome)
    aposta = validar_aposta(ficha_do_jogador['carteira']['saldo'])
    if aposta is None:
        print('Por isso não foi possível apostar.')
    else:
        ficha_do_jogador['carteira']['saldo'] -= aposta
        ficha_do_jogador['carteira']['extrato'].append((f'Aposta {jogo_nome}', -aposta))
        resultado = jogo()
        ficha_do_jogador['estatisticas_gerais']['partidas_totais'] += 1
        ficha_do_jogador['estatisticas_jogos'][jogo_estatisticas]['partidas'] += 1
        atualizar_aposta(ficha_do_jogador, aposta, resultado, jogo_estatisticas)

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
                gerencia_partidas('JOKENPÔ', jokenpo.jokenpo, 'jokenpo')

            elif escolha_jogo == 2:
                gerencia_partidas('PAR OU ÍMPAR', par_ou_impar.par_ou_impar, 'par_ou_impar')


            elif escolha_jogo == 3:
                cabeçalho('ADIVINHE O NÚMERO')

    elif escolha_principal == 2:
        cabeçalho('PERFIL')
        

    elif escolha_principal == 3:
        cabeçalho('CARTEIRA')
        print(f'Saldo atual: R${ficha_do_jogador["carteira"]["saldo"]} ')
        escolha_carteira = menu(lista=['VOLTAR', 'DEPOSITAR', 'SACAR', 'EXTRATO'], menu_titulo='')
        if escolha_carteira == 0:
            cabeçalho('VOLTANDO')

        elif escolha_carteira == 1:
            cabeçalho('DEPOSITAR')
            ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['carteira']['extrato'] = depositar(ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['carteira']['extrato'])

        elif escolha_carteira == 2:
            cabeçalho('SACAR')
            ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['carteira']['extrato'] = sacar(ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['carteira']['extrato'])

        elif escolha_carteira == 3:
            cabeçalho('EXTRATO')
            mostrar_extrato(ficha_do_jogador['carteira']['extrato'], ficha_do_jogador['carteira']['saldo'])


