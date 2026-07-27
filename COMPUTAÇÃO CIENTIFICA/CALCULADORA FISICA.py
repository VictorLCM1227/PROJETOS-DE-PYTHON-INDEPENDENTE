def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número interiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

def leiaFloatPositivo(msg):
    while True:
        try:
            numero = float(input(msg))    
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            if numero > 0:
                return numero
            print('\033[31mERRO: por favor, digite um número real válido e maior do que zero.\033[m')

def linha(simbolo='-', tam = 42):
    return simbolo * tam 

def cabecalho(txt, simbolo='-'):
    print(linha(simbolo))
    print(txt.center(42))
    print(linha(simbolo))

def menu(lista, menu_msg='MENU PRINCIPAL'):
    cabecalho(menu_msg)
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

def calcular_velocidade():
    distancia_percorrida = leiaFloatPositivo('Distância percorrida em Km: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em horas: ')
    velocidade = distancia_percorrida / tempo_gasto
    print(linha())
    print('Fórmula:')
    print('v = Δs / Δt')
    print('Substituindo:')
    print(f'v = {distancia_percorrida} km / {tempo_gasto} h')
    print('Resultado:')
    print(f'v = {velocidade:.2f} km/h')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_distancia():
    velocidade = leiaFloatPositivo('Velocidade em Km/h: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em horas: ')
    distancia_percorrida = velocidade * tempo_gasto
    print(linha())
    print('Fórmula:')
    print('Δs = v × t')
    print('Substituindo:')
    print(f'Δs = {velocidade} km/h × {tempo_gasto} h')
    print('Resultado:')
    print(f'Δs = {distancia_percorrida:.2f} km')
    print(linha())
    input('Pressione ENTER para continuar...')

def Calcular_tempo():
    distancia_percorrida = leiaFloatPositivo('Distância percorrida em Km: ')
    velocidade = leiaFloatPositivo('Velocidade em Km/h: ')
    tempo_gasto = distancia_percorrida / velocidade
    print(linha())
    print('Fórmula:')
    print('Δt = Δs / v')
    print('Substituindo:')
    print(f'Δt = {distancia_percorrida} km / {velocidade} km/h')
    print('Resultado:')
    print(f'Δt = {tempo_gasto:.2f} h')
    print(linha())
    input('Pressione ENTER para continuar...')


def calcular_velocidade_final():
    velocidade_inicial = leiaFloatPositivo('Velocidade inicial em Km/h: ')
    aceleracao = leiaFloatPositivo('Aceleração em km/h²: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em horas: ')
    velocidade_final = velocidade_inicial + aceleracao * tempo_gasto   
    print(linha())
    print('Fórmula:')
    print('v = v₀ + a × t')
    print('Substituindo:')
    print(f'v = {velocidade_inicial} km/h  + {aceleracao} km/h² x {tempo_gasto} h')
    print('Resultado:')
    print(f'v = {velocidade_final:.2f} km/h')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_aceleracao():

while True:
    cabecalho('CALCULADORA DE FÍSICA', simbolo='=')
    opcao_menu = menu(['SAIR', 'MRU', 'MRUV'])

    if opcao_menu == 0:
        cabecalho('SAIR')
        break

    elif opcao_menu == 1:
        while True:
            opcao_submenu = menu(['Voltar', 'Calcular velocidade', 'Calcular distância', 'Calcular tempo'], menu_msg='MENU MRU')
            if opcao_submenu == 0:
                cabecalho('VOLTANDO')
                break
            elif opcao_submenu == 1:
                cabecalho('Calcular velocidade')
                calcular_velocidade()

            elif opcao_submenu == 2:
                cabecalho('Calcular distância')
                calcular_distancia()
            elif opcao_submenu == 3:
                cabecalho('Calcular tempo')
                Calcular_tempo()
            else:
                print('Opção inválida.')
        
    elif opcao_menu == 2:
        while True:
            opcao_submenu_mruv = menu(['Voltar', 'Velocidade final', 'Aceleração', 'Tempo', 'Deslocamento', 'Torricelli'], menu_msg='MENU MRUV')
            if opcao_submenu_mruv == 0:
                cabecalho('Voltar')
                break
            elif opcao_submenu_mruv == 1:
                cabecalho('Velocidade final')
                calcular_velocidade_final()
            elif opcao_submenu_mruv == 2:
                cabecalho('Aceleração')
            elif opcao_submenu_mruv == 3:
                cabecalho('Tempo')
            elif opcao_submenu_mruv == 4:
                cabecalho('Deslocamento')
            elif opcao_submenu_mruv == 5:
                cabecalho('Torricelli')
            else:
                print('Opção inválida.')

    else:
        print('Opção inválida.')