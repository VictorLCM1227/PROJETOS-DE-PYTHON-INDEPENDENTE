from random import randint
from time import sleep

cavalos = ['Caddlac', 'Princesa']
cavalo0 = cavalo1 = 1
linha_de_chegada = 35
contador = 0

def linha(tam = 42):
    return '-' * tam 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 0
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
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
    aposta_jogador = menu(cavalos)
    if 0 <= aposta_jogador <= 1:
        break
    print('Opção inválida! Escolha um cavalo de 0 a 1: ')
aposta_computador = randint(0, 1)

while True:
    print(f'ROUND {contador + 1}')
    cavalo0 += randint(1, 5)
    cavalo1 += randint(1, 5)
    #pista 35 casas
    if cavalo0 > linha_de_chegada:
        cavalo0 = linha_de_chegada
    if cavalo1 > linha_de_chegada:
        cavalo1 = linha_de_chegada
    print(f'{cavalos[0]:8}:{" "*(cavalo0 - 1)}🐎{" "*(linha_de_chegada - cavalo0)}|🏁')
    print(f'{cavalos[1]:8}:{" "*(cavalo1 - 1)}🐎{" "*(linha_de_chegada - cavalo1)}|🏁')
    print('-=-' * 20)
    sleep(1)
    if cavalo0 >= linha_de_chegada or cavalo1 >= linha_de_chegada:
        break
    contador +=1 

if cavalo0 > cavalo1:
    print(f'O CAVALO {cavalos[0]} VENCEU A CORRIDA!')
    vencedor = 0
elif cavalo1 > cavalo0:
    print(f'O CAVALO {cavalos[1]} VENCEU A CORRIDA!')
    vencedor = 1
else:
    print('HOUVE EMPATE! CORRIDA ANULADA!')
    vencedor = 2

if aposta_jogador == aposta_computador:
    print('JOGADOR e COMPUTADOR fizeram a mesma aposta!')
else:
    if aposta_jogador == vencedor:
        print('JOGADOR VENCEU A APOSTA!')
#aposta
    elif aposta_computador == vencedor:
        print('COMPUTADOR VENCEU A APOSTA!')
    else:
        print('NINGUÉM venceu a aposta!')


print(f'Você apostou no cavalo {aposta_jogador} e o computador no cavalo {aposta_computador}.')