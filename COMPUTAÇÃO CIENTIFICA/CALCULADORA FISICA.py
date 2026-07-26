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

def linha(simbolo='-', tam = 42):
    return simbolo * tam 

def cabecalho(txt, simbolo='-'):
    print(linha(simbolo))
    print(txt.center(42))
    print(linha(simbolo))

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

cabecalho('CALCULADORA DE FÍSICA', simbolo='=')
opcao_menu = menu(['SAIR', 'MRU', 'MRUV'])

if opcao_menu == 0:
    cabecalho('SAIR')
elif opcao_menu == 1:
    cabecalho('MRU')
    opcao_submenu = menu(['Voltar', 'Calcular velocidade', 'Calcular distância', 'Calcular tempo'])
    if opcao_submenu == 0:
        cabecalho('VOLTANDO')
    elif opcao_submenu == 1:
        cabecalho('Calcular velocidade')
    
elif opcao_menu == 2:
    cabecalho('MRUV')
    opcao_submenu = menu(['Voltar', 'Velocidade final', 'Aceleração', 'Tempo', 'Deslocamento', 'Torricelli'])