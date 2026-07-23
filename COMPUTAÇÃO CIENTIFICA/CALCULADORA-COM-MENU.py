from time import sleep

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
            print('\033[31mERRO: por favor, digite um número interiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

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
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

def somar(numeros):

while True:
    numeros = []
    cabeçalho('CALCULADORA')
    resposta_menu = menu(['Sair', 'Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Potência', 
                     'Raiz quadrada', 'Resto da divisão', 'Divisão inteira',
                     'Histórico'])
    if resposta_menu == 0:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    elif resposta_menu == 1:
        while True:


    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    