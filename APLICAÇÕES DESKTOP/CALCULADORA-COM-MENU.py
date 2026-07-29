from time import sleep

historico = []

def pegar_numero(msg1, msg2):
    numero1 = leiaFloat(msg1)
    numero2 = leiaFloat(msg2)
    return numero1, numero2

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

def adiciona_ao_historico(mostrar):
        print(mostrar)
        historico.append(mostrar)
     
def somar():
        cabeçalho('SOMAR')
        numeros = pegar_numero('Digite o primeiro número: ', 'Digite um número para somar ao primeiro: ')
        resultado = sum(numeros)
        mostrar = f'A soma entre {numeros[0]} e {numeros[1]} deu {resultado}'
        adiciona_ao_historico(mostrar)

def subtrair():
        cabeçalho('SUBTRAIR')
        numeros = pegar_numero('Digite o primeiro número: ', 'Digite um número para subtrair ao primeiro: ')
        resultado = numeros[0] - numeros[1]
        mostrar = (f'A subtração entre {numeros[0]} e {numeros[1]} deu {resultado}')
        adiciona_ao_historico(mostrar)
        
def multiplicar():
        cabeçalho('MULTIPLICAR')
        numeros = pegar_numero('Digite o primeiro número: ', 'Digite um número para multiplicar o primeiro: ')
        resultado = numeros[0] * numeros[1]
        mostrar = (f'A multiplicação entre {numeros[0]} e {numeros[1]} deu {resultado}')
        adiciona_ao_historico(mostrar)

def dividir():
        cabeçalho('DIVIDIR')
        numeros = pegar_numero('Digite o primeiro número: ', 'Digite um número para dividir o primeiro: ')
        try:
            resultado = numeros[0] / numeros[1]
        except ZeroDivisionError:
             print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'A divisão entre {numeros[0]} e {numeros[1]} deu {resultado}'
            adiciona_ao_historico(mostrar)

def potencia():
        cabeçalho('POTÊNCIA')
        numeros = pegar_numero('Digite a base: ', 'Digite o seu expoente: ')
        resultado = numeros[0] ** numeros[1]
        mostrar = f'O {numeros[0]} elevado a {numeros[1]} é igual a {resultado}'
        adiciona_ao_historico(mostrar)

def raiz():
        cabeçalho('RAIZ')
        while True:
            numero1 = leiaFloat('Digite o radicando: ')
            if numero1 >= 0:
                break
            print('O radicando deve ser maior ou igual a zero.')
            #verificação com while True
        while True:   
            numero2 = leiaFloat('Digite a raiz: ')
            if numero2 > 0:
                break
            print('A raiz deve ser maior que zero.')
        resultado = numero1 **  (1 / numero2)
        mostrar = f'A raiz {numero2} de {numero1} é igual a {resultado:.2f}'
        adiciona_ao_historico(mostrar)

def resto_da_divisao():
        cabeçalho('RESTO DA DIVISÃO')
        numeros = pegar_numero('Digite o dividendo: ', 'Digite o divisor: ')
        try:
            resultado = numeros[0] % numeros[1]
        except ZeroDivisionError:
            print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'O resto de {numeros[0]} dividido por  {numeros[1]} é igual a {resultado}'
            adiciona_ao_historico(mostrar)

def divisao_inteira():
        cabeçalho('DIVISÃO INTEIRA')
        numeros = pegar_numero('Digite o primeiro número: ', 'Digite um número para dividir o primeiro: ')
        try:
            resultado = numeros[0] // numeros[1]
        except ZeroDivisionError:
             print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'A divisão inteira entre {numeros[0]} e {numeros[1]} deu {resultado}'
            adiciona_ao_historico(mostrar)

def mostrar_historico():
    cabeçalho('HISTÓRICO')
    contador = 1
    if not historico:
         print('Nenhuma operação realizada')
    else:
        for operacao in historico:
            print(f'\033[33m{contador}\033[m - \033[34m{operacao}\033[m')
            contador += 1
        print(linha())

cabeçalho('CALCULADORA')
while True:
    resposta_menu = menu(['Sair', 'Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Potência', 
                     'Raiz', 'Resto da divisão', 'Divisão inteira',
                     'Histórico'])
    if resposta_menu == 0:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    elif resposta_menu == 1:
       somar()
    elif resposta_menu == 2:
        subtrair()
    elif resposta_menu == 3:
        multiplicar()
    elif resposta_menu == 4:
         dividir()
    elif resposta_menu == 5:
         potencia()
    elif resposta_menu == 6:
         raiz()
    elif resposta_menu == 7:
         resto_da_divisao()
    elif resposta_menu == 8:
         divisao_inteira()
    elif resposta_menu == 9:
        mostrar_historico()
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
    