from math import sqrt

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
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
        except ValueError:
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
        except ValueError:
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
    distancia_percorrida = leiaFloatPositivo('Distância percorrida em m: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em segundos: ')
    velocidade = distancia_percorrida / tempo_gasto
    print(linha())
    print('Fórmula:')
    print('v = Δs / Δt')
    print('Substituindo:')
    print(f'v = {distancia_percorrida} m / {tempo_gasto} s')
    print('Resultado:')
    print(f'v = {velocidade:.2f} m/s')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_distancia():
    velocidade = leiaFloatPositivo('Velocidade em m/s: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em segundos: ')
    distancia_percorrida = velocidade * tempo_gasto
    print(linha())
    print('Fórmula:')
    print('Δs = v × t')
    print('Substituindo:')
    print(f'Δs = {velocidade} m/s × {tempo_gasto} s')
    print('Resultado:')
    print(f'Δs = {distancia_percorrida:.2f} m')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_tempo():
    distancia_percorrida = leiaFloatPositivo('Distância percorrida em m: ')
    velocidade = leiaFloatPositivo('Velocidade em m/s: ')
    tempo_gasto = distancia_percorrida / velocidade
    print(linha())
    print('Fórmula:')
    print('Δt = Δs / v')
    print('Substituindo:')
    print(f'Δt = {distancia_percorrida} m / {velocidade} m/s')
    print('Resultado:')
    print(f'Δt = {tempo_gasto:.2f} s')
    print(linha())
    input('Pressione ENTER para continuar...')


def calcular_velocidade_final():
    velocidade_inicial = leiaFloat('Velocidade inicial em m/s: ')
    aceleracao = leiaFloat('Aceleração em m/s²: ')
    tempo_gasto = leiaFloatPositivo('Tempo gasto em segundos: ')
    velocidade_final = velocidade_inicial + aceleracao * tempo_gasto   
    print(linha())
    print('Fórmula:')
    print('v = v₀ + a × t')
    print('Substituindo:')
    print(f'v = {velocidade_inicial} m/s  + {aceleracao} m/s² x {tempo_gasto} s')
    print('Resultado:')
    print(f'v = {velocidade_final:.2f} m/s')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_aceleracao():
    velocidade_final = leiaFloat('Velocidade final em m/s: ')
    velocidade_inicial = leiaFloat('Velocidade inicial em m/s: ')
    tempo = leiaFloatPositivo('Tempo gasto em segundos: ')
    aceleracao = (velocidade_final - velocidade_inicial) / tempo
    print(linha())
    print('Fórmula:')
    print('a = (v - v0) / t')
    print('Substituindo:')
    print(f'a = ({velocidade_final} - {velocidade_inicial}) / {tempo}')
    print('Resultado:')
    print(f'a = {aceleracao:.2f} m/s²')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_tempo_mruv():
    velocidade_final = leiaFloat('Velocidade final em m/s: ')
    velocidade_inicial = leiaFloat('Velocidade inicial em m/s: ')
    aceleracao = leiaFloat('Aceleração em m/s²: ')
    try:
        tempo = (velocidade_final - velocidade_inicial) / aceleracao
    except ZeroDivisionError:
        print('Não foi possível dividir por 0.')
    else:
        print(linha())
        print('Fórmula:')
        print('t = (v - v0) / a')
        print('Substituindo:')
        print(f't = ({velocidade_final} - {velocidade_inicial}) / {aceleracao}')
        print('Resultado:')
        print(f't = {tempo:.2f} s')
        print(linha())
        input('Pressione ENTER para continuar...')

def calcular_deslocamento():
    velocidade = leiaFloat('Velocidade inicial em m/s: ')
    tempo = leiaFloatPositivo('Tempo gasto em segundos: ')
    aceleracao = leiaFloat('Aceleração em m/s²: ')
    deslocamento = velocidade * tempo + ((aceleracao * tempo**2) / 2)
    print(linha())
    print('Fórmula:')
    print('s = v0t + (at²)/2')
    print('Substituindo:')
    print(f's = {velocidade} x {tempo} + ({aceleracao} x {tempo**2})/2')
    print('Resultado:')
    print(f's = {deslocamento:.2f} m')
    print(linha())
    input('Pressione ENTER para continuar...')

def calcular_torricelli():
    while True:
        opcao = menu(['Voltar', 'Velocidade final', 'Deslocamento'], menu_msg='TORRICELLI')
        if opcao == 0:
            cabecalho('Voltar')
            break
        elif opcao == 1:
            cabecalho('velocidade final')
            velocidade_inicial = leiaFloat('Velocidade inicial em m/s: ')
            aceleracao = leiaFloat('Aceleração em m/s²: ')
            distancia_percorrida = leiaFloatPositivo('Distância percorrida em m: ')
            try:
                velocidade_final = sqrt(velocidade_inicial**2 + 2 * aceleracao * distancia_percorrida)
            except ValueError:
                print('A resposta não existe no conjunto dos números reais.')
            else:
                print(linha())
                print('Fórmula:')
                print('v = √(v0² + 2*a*Δs)')
                print('Substituindo:')
                print(f'v = √({velocidade_inicial}² + 2 * {aceleracao} * {distancia_percorrida})')
                print('Resultado:')
                print(f'v = {velocidade_final:.2f} m/s')
                print(linha())
                input('Pressione ENTER para continuar...')

        elif opcao == 2:
            cabecalho('deslocamento')
            velocidade_inicial = leiaFloat('Velocidade inicial em m/s: ')
            velocidade_final = leiaFloat('Velocidade final em m/s: ')
            aceleracao = leiaFloat('Aceleração em m/s²: ')
            try:
                deslocamento = (velocidade_final**2 - velocidade_inicial**2) / (2 * aceleracao)
            except ZeroDivisionError:
                print('Não é possível calcular deslocamento com aceleração igual a zero.')
            else:
                print(linha())
                print('Fórmula:')
                print('Δs = (v² - v0²) / (2 x a)')
                print('Substituindo:')
                print(f'Δs = ({velocidade_final}² - {velocidade_inicial}²) / (2 x {aceleracao})')
                print('Resultado:')
                print(f's = {deslocamento:.2f} m')
                print(linha())
                input('Pressione ENTER para continuar...')

        else:
            print('Opção inválida.')

while True:
    cabecalho('CALCULADORA DE FÍSICA', simbolo='=')
    opcao_menu = menu(['SAIR', 'MRU', 'MRUV'])

    if opcao_menu == 0:
        cabecalho('SAINDO')
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
                calcular_tempo()
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
                calcular_aceleracao()
            elif opcao_submenu_mruv == 3:
                cabecalho('Tempo')
                calcular_tempo_mruv()
            elif opcao_submenu_mruv == 4:
                cabecalho('Deslocamento')
                calcular_deslocamento()
            elif opcao_submenu_mruv == 5:
                cabecalho('Torricelli')
                calcular_torricelli()
            else:
                print('Opção inválida.')

    else:
        print('Opção inválida.')

#adiconar conversor de medidas de m pra km