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

def menu(lista, menu_msg='MENU PRINCIPAL'):
    cabecalho(menu_msg)
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

#terminar
def menu_mru_mruv(cabecalho_menu='MRU', menu_lista=['Voltar', 'Calcular velocidade', 'Calcular distância', 'Calcular tempo'],novo_menu_msg='MENU MRU'):
    while True:
        cabecalho(cabecalho_menu)
        opcao_submenu = menu(menu_lista, menu_msg=novo_menu_msg)
        for chave, item in enumerate(menu_lista):
            if opcao_submenu == chave:
                cabecalho(item)
            #criar funcao pra cada opcao e chamar conforme o item que essa funcao vai retornar
        if opcao_submenu == 0:
            cabecalho('VOLTANDO')
            break
        elif opcao_submenu == 1:
            cabecalho('Calcular velocidade')
        elif opcao_submenu == 2:
            cabecalho('Calcular distância')
        elif opcao_submenu == 3:
            cabecalho('Calcular tempo')

while True:
    cabecalho('CALCULADORA DE FÍSICA', simbolo='=')
    opcao_menu = menu(['SAIR', 'MRU', 'MRUV'])

    if opcao_menu == 0:
        cabecalho('SAIR')
        break

    elif opcao_menu == 1:
        while True:
            cabecalho('MRU')
            opcao_submenu = menu(['Voltar', 'Calcular velocidade', 'Calcular distância', 'Calcular tempo'], menu_msg='MENU MRU')
            if opcao_submenu == 0:
                cabecalho('VOLTANDO')
                break
            elif opcao_submenu == 1:
                cabecalho('Calcular velocidade')
            elif opcao_submenu == 2:
                cabecalho('Calcular distância')
            elif opcao_submenu == 3:
                cabecalho('Calcular tempo')
        
    elif opcao_menu == 2:
        while True:
            cabecalho('MRUV')
            opcao_submenu_mruv = menu(['Voltar', 'Velocidade final', 'Aceleração', 'Tempo', 'Deslocamento', 'Torricelli'], menu_msg='MENU MRUV')
            if opcao_submenu_mruv == 0:
                cabecalho('Voltar')
                break
            elif opcao_submenu_mruv == 1:
                cabecalho('Velocidade final')
            elif opcao_submenu_mruv == 2:
                cabecalho('Aceleração')
            elif opcao_submenu_mruv == 3:
                cabecalho('Tempo')
            elif opcao_submenu_mruv == 4:
                cabecalho('Deslocamento')
            elif opcao_submenu_mruv == 5:
                cabecalho('Torricelli')