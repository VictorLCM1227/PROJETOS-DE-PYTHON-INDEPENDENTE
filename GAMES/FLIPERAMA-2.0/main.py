#menu principal

from perfil import mostrar_perfil, ver_estatisticas_dos_jogos, ver_conquistas
from carteira import depositar, sacar, mostrar_extrato, validar_aposta, atualizar_aposta
from utilidades import cabeçalho, menu
from jogador import ficha_do_jogador
from jogos import jokenpo, par_ou_impar, advinhe_o_numero, corrida, blackjack, dados
from jogos.jogo_da_forca_pasta import jogo_da_forca_arquivo
from jogos.jogo_da_velha_pasta import jogo_da_velha_arquivo
from conquistas import controla_conquistas

def gerencia_partidas(jogo_nome, jogo, jogo_estatisticas):
    cabeçalho(jogo_nome)
    aposta = validar_aposta(ficha_do_jogador['carteira']['saldo'])
    if aposta is None:
        print('Por isso não foi possível apostar.')
    else:
        ficha_do_jogador['carteira']['saldo'] -= aposta
        ficha_do_jogador['extrato'].append((f'Aposta {jogo_estatisticas}', -aposta))
        resultado = jogo()
        ficha_do_jogador['estatisticas_gerais']['partidas_totais'] += 1
        ficha_do_jogador['estatisticas_jogos'][jogo_estatisticas]['partidas'] += 1
        atualizar_aposta(ficha_do_jogador, aposta, resultado, jogo_estatisticas)
        controla_conquistas(ficha_do_jogador)


print('BEM VINDO!!!')


while True:
    escolha_principal = menu(lista=['SAIR', 'JOGAR', 'PERFIL', 'CARTEIRA', 'LOJA'], menu_titulo='FLIPERAMA DO VICTOR')

    if escolha_principal == 0:
        cabeçalho('SAINDO')
        break

    elif escolha_principal == 1:
        cabeçalho('JOGAR')
        while True:
            escolha_jogo = menu(lista=['VOLTAR', 'JOKENPÔ', 'PAR OU ÍMPAR', 'ADIVINHE O NÚMERO',
                                    'CORRIDA DE CAVALOS', 'BLACKJACK', 'DADOS', 'JOGO DA FORCA', 'JOGO DA VELHA'], menu_titulo='JOGOS')

            if escolha_jogo == 0:
                cabeçalho('VOLTANDO')
                break

            elif escolha_jogo == 1:
                gerencia_partidas('JOKENPÔ', jokenpo.jokenpo, 'jokenpo')

            elif escolha_jogo == 2:
                gerencia_partidas('PAR OU ÍMPAR', par_ou_impar.par_ou_impar, 'par_ou_impar')


            elif escolha_jogo == 3:
                gerencia_partidas('ADIVINHE O NÚMERO', advinhe_o_numero.adivinhe_o_numero, 'adivinhe_o_numero')

            elif escolha_jogo == 4:
                gerencia_partidas('CORRIDA DE CAVALOS',corrida.corrida_de_cavalos,'corrida_de_cavalos')

            elif escolha_jogo == 5:
                gerencia_partidas('BLACKJACK',blackjack.blackjack_21,'blackjack')

            elif escolha_jogo == 6:
                gerencia_partidas('DADOS',dados.jogo_de_dados,'jogo-de-dados')

            elif escolha_jogo == 7:
                gerencia_partidas('JOGO DA FORCA',jogo_da_forca_arquivo.jogo_da_forca_funcao,'jogo-da-forca')

            elif escolha_jogo == 8:
                gerencia_partidas('JOGO DA VELHA',jogo_da_velha_arquivo.jogo_da_velha_funcao,'jogo-da-velha')

    elif escolha_principal == 2:
        cabeçalho('PERFIL')
        while True:
            escolha_perfil = menu(lista=['VOLTAR', 'VER PERFIL GERAL', 'VER ESTATÍSTICAS DOS JOGOS',
            'VER CONQUISTAS'], menu_titulo='PERFIL')
            if escolha_perfil == 0:
                cabeçalho('VOLTANDO')
                break
                
            elif escolha_perfil == 1:
                mostrar_perfil(ficha_do_jogador)
                
            elif escolha_perfil == 2:
                cabeçalho('ESTATÍSTICAS DOS JOGOS')
                ver_estatisticas_dos_jogos(ficha_do_jogador)
                
            elif escolha_perfil == 3:
                cabeçalho('CONQUISTAS')
                ver_conquistas(ficha_do_jogador)
        

    elif escolha_principal == 3:
        cabeçalho('CARTEIRA')
        while True:
            print(f'Saldo atual: R${ficha_do_jogador["carteira"]["saldo"]} ')
            escolha_carteira = menu(lista=['VOLTAR', 'DEPOSITAR', 'SACAR', 'EXTRATO'], menu_titulo='CARTEIRA')
            if escolha_carteira == 0:
                cabeçalho('VOLTANDO')
                break

            elif escolha_carteira == 1:
                cabeçalho('DEPOSITAR')
                ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['extrato'] = depositar(ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['extrato'])

            elif escolha_carteira == 2:
                cabeçalho('SACAR')
                ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['extrato'] = sacar(ficha_do_jogador['carteira']['saldo'], ficha_do_jogador['extrato'])

            elif escolha_carteira == 3:
                cabeçalho('EXTRATO')
                mostrar_extrato(ficha_do_jogador['extrato'], ficha_do_jogador['carteira']['saldo'])


    elif escolha_principal == 4:
        cabeçalho('LOJA')
        while True:
            escolha_loja = menu(lista=['VOLTAR','COR DE FUNDO', 'COR DE FONTE', 'EMOJI'], menu_titulo='LOJA')

            if escolha_loja == 0:
                cabeçalho('VOLTANDO')
                break

            elif escolha_loja == 1:
                while True:
                    cabeçalho('COR DE FUNDO')
                    escolha_fundo = menu(lista=['VOLTAR','LISTAR CORES DE FUNDO', 'COMPRAR CORES DE FUNDO'], menu_titulo='COR DE FUNDO')
                    if escolha_fundo == 0:
                        break

            elif escolha_loja == 2:
                while True:
                    cabeçalho('COR DE FONTE')
                    escolha_fonte = menu(lista=['VOLTAR','LISTAR CORES DE FONTE', 'COMPRAR CORES DE FONTE'], menu_titulo='COR DE FONTE')
                    if escolha_fonte == 0:
                        break

            elif escolha_loja == 3:
                while True:
                    cabeçalho('EMOJI')
                    escolha_emoji = menu(lista=['VOLTAR','LISTAR EMOJIs', 'COMPRAR EMOJIs'], menu_titulo='EMOJI')
                    if escolha_emoji == 0:
                        break


