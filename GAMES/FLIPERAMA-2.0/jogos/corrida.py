#corrida de cavalos

from random import randint
from time import sleep
from utilidades import cabeçalho, menu_corrida

def corrida_de_cavalos():
    corrida_terminou = False

    cavalos_dicionario = {
        'Caddlac': {
            'velocidade': 5,
            'sorte': 3,
            'vitorias': 0,
            'posicao': 0
        },

        'Princesa': {
            'velocidade': 7,
            'sorte': 3,
            'vitorias': 0,
            'posicao': 0
        }
    }
    nomes_cavalos = list(cavalos_dicionario.keys())
    linha_de_chegada = 35

    cabeçalho('CORRIDA DE CAVALOS')
    while True:
        aposta_jogador = menu_corrida(cavalos_dicionario)
        if 0 <= aposta_jogador <= 1:
            break
        print('Opção inválida! Escolha um cavalo de 0 a 1: ')
    aposta_jogador_nome = nomes_cavalos[aposta_jogador]

    while not corrida_terminou:
        for nome in nomes_cavalos:
            cavalos_dicionario[nome]['posicao'] += randint(1, cavalos_dicionario[nome]['velocidade'])
        #pista 35 casas
        if cavalos_dicionario['Caddlac']['posicao'] > linha_de_chegada:
            cavalos_dicionario['Caddlac']['posicao'] = linha_de_chegada
        if cavalos_dicionario['Princesa']['posicao'] > linha_de_chegada:
            cavalos_dicionario['Princesa']['posicao'] = linha_de_chegada
        print(f'{nomes_cavalos[0]:8}:{" "*(cavalos_dicionario["Caddlac"]["posicao"] - 1)}🐎{" "*(linha_de_chegada - cavalos_dicionario["Caddlac"]["posicao"])}|🏁')
        print(f'{nomes_cavalos[1]:8}:{" "*(cavalos_dicionario["Princesa"]["posicao"] - 1)}🐎{" "*(linha_de_chegada - cavalos_dicionario["Princesa"]["posicao"])}|🏁')
        print('-=-' * 20)
        sleep(1)
        for cavalos in nomes_cavalos:
            if cavalos_dicionario[cavalos]['posicao'] >= linha_de_chegada:
                corrida_terminou = True
                break

    if cavalos_dicionario['Caddlac']['posicao'] > cavalos_dicionario['Princesa']['posicao']:
        print(f'O CAVALO {nomes_cavalos[0]  } VENCEU A CORRIDA!')
        vencedor = nomes_cavalos[0]
    elif cavalos_dicionario['Princesa']['posicao'] > cavalos_dicionario['Caddlac']['posicao']:
        print(f'O CAVALO {nomes_cavalos[1]} VENCEU A CORRIDA!')
        vencedor = nomes_cavalos[1]
    else:
        print('HOUVE EMPATE! CORRIDA ANULADA!')
        vencedor = 'NINGUÉM'


    if aposta_jogador_nome == vencedor:
        print('VOCÊ VENCEU A APOSTA!')
        return 'V'
        
    else:
        print('VOCÊ PERDEU A APOSTA!')
        return 'D'
