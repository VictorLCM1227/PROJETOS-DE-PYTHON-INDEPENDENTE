from random import randint
from time import sleep

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
contador = 0

def linha(tam = 42):
    return '-' * tam 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(dicionario):
    cabeçalho('MENU PRINCIPAL')
    contador = 0
    for chave in dicionario.keys():
        print(f'\033[33m{contador}\033[m - \033[34m{chave}\033[m')
        for atributo, valor in dicionario[chave].items():
            print(f'{atributo} : {valor}')
        print()
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32m>>>Em qual cavalo deseja apostar? \033[m')
    return opcao

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

cabeçalho('CORRIDA DE CAVALOS')
while True:
    aposta_jogador = menu(cavalos_dicionario)
    if 0 <= aposta_jogador <= 1:
        break
    print('Opção inválida! Escolha um cavalo de 0 a 1: ')
aposta_computador = randint(0, 1)
aposta_jogador_nome = nomes_cavalos[aposta_jogador]
aposta_computador_nome = nomes_cavalos[aposta_computador]

while True:
    print(f'ROUND {contador + 1}')
    for nome in nomes_cavalos:
        cavalos_dicionario[nome]['posicao'] += randint(1, cavalos_dicionario[nome]['velocidade'])
    #pista 35 casas
    if cavalos_dicionario['Caddlac']['posicao'] > linha_de_chegada:
        cavalos_dicionario['Caddlac']['posicao'] = linha_de_chegada
    if cavalos_dicionario['Princesa']['posicao'] > linha_de_chegada:
        cavalos_dicionario['Princesa']['posicao'] = linha_de_chegada
    print(f'{nomes_cavalos[0]:8}:{" "*(cavalos_dicionario['Caddlac']['posicao'] - 1)}🐎{" "*(linha_de_chegada - cavalos_dicionario['Caddlac']['posicao'])}|🏁')
    print(f'{nomes_cavalos[1]:8}:{" "*(cavalos_dicionario['Princesa']['posicao'] - 1)}🐎{" "*(linha_de_chegada - cavalos_dicionario['Princesa']['posicao'])}|🏁')
    print('-=-' * 20)
    sleep(1)
    for cavalos in nomes_cavalos:
        if cavalos_dicionario[cavalos]['posicao'] >= linha_de_chegada:
            break
    contador +=1 

if cavalos_dicionario['Caddlac']['posicao'] > cavalos_dicionario['Princesa']['posicao']:
    print(f'O CAVALO {cavalos['Caddlac']} VENCEU A CORRIDA!')
    vencedor = nomes_cavalos[0]
elif cavalos_dicionario['Princesa']['posicao'] > cavalos_dicionario['Caddlac']['posicao']:
    print(f'O CAVALO {cavalos['Princesa']} VENCEU A CORRIDA!')
    vencedor = nomes_cavalos[1]
else:
    print('HOUVE EMPATE! CORRIDA ANULADA!')
    vencedor = 'NINGUÉM'

if aposta_jogador_nome == aposta_computador_nome:
    print('JOGADOR e COMPUTADOR fizeram a mesma aposta!')
else:
    if aposta_jogador_nome == vencedor:
        print('JOGADOR VENCEU A APOSTA!')
#aposta
    elif aposta_computador_nome == vencedor:
        print('COMPUTADOR VENCEU A APOSTA!')
    else:
        print('NINGUÉM venceu a aposta!')


print(f'Você apostou no cavalo {nomes_cavalos[aposta_jogador]} e o computador no cavalo {nomes_cavalos[aposta_computador]}.')


#voltar a mexer quando eu aprender melhor python poo