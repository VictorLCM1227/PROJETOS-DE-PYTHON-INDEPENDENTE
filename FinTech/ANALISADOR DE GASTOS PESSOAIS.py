
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

while True:
    opcao = menu(['Sair', 'Adicionar gasto', 'Listar gastos', 'Ver total gasto',
                   'Ver gastos por categoria', 'Maior gasto', 'Média dos gastos'], menu_msg='CONTROLE FINANCEIRO')

    if opcao == 0:
        cabecalho('Saindo')
        break
    if opcao == 1:
        cabecalho('Adicionar gasto')
        
    if opcao == 2:
        cabecalho('Listar gastos')
        
    if opcao == 3:
        cabecalho('Ver total gasto')

    if opcao == 4:
        cabecalho('Ver gastos por categoria')

    if opcao == 5:
        cabecalho('Maior gasto')

    if opcao == 6:
        cabecalho('Média dos gastos')
