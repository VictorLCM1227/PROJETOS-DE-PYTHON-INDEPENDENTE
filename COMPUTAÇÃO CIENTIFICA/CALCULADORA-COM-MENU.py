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

def gera_historico(mostrar):
        print(mostrar)
        historico.append(mostrar)
     
def somar():
        cabeçalho('SOMAR')
        numero1 = leiaFloat('Digite o primeiro número: ')
        numero2 = leiaFloat('Digite um número para somar ao primeiro: ')
        resultado = numero1 + numero2
        mostrar = f'A soma entre {numero1} e {numero2} deu {resultado}'
        gera_historico(mostrar)

def subtrair():
        cabeçalho('SUBTRAIR')
        numero1 = leiaFloat('Digite o primeiro número: ')
        numero2 = leiaFloat('Digite um número para subtrair do primeiro: ')
        resultado = numero1 - numero2
        mostrar = (f'A subtração entre {numero1} e {numero2} deu {resultado}')
        gera_historico(mostrar)
        

def multiplicar():
        cabeçalho('MULTIPLICAR')
        numero1 = leiaFloat('Digite o primeiro número: ')
        numero2 = leiaFloat('Digite um número para multiplicar o primeiro: ')
        resultado = numero1 * numero2
        mostrar = (f'A multiplicação entre {numero1} e {numero2} deu {resultado}')
        gera_historico(mostrar)

def dividir():
        cabeçalho('DIVIDIR')
        numero1 = leiaFloat('Digite o primeiro número: ')
        numero2 = leiaFloat('Digite um número para dividir o primeiro: ')
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
             print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'A divisão entre {numero1} e {numero2} deu {resultado}'
            gera_historico(mostrar)

def potencia():
        cabeçalho('POTÊNCIA')
        numero1 = leiaFloat('Digite a base: ')
        numero2 = leiaFloat('Digite o seu expoente: ')
        resultado = numero1 ** numero2
        mostrar = f'O {numero1} elevado a {numero2} é igual a {resultado}'
        gera_historico(mostrar)

def raiz():
        cabeçalho('RAIZ')
        while True:
            numero1 = leiaFloat('Digite o radicando: ')
            if numero1 > 0:
                break
            print('D')
            #verificação com while True
            
        numero2 = leiaFloat('Digite a raiz: ')
        if numero2 <= 0:
            print('Não existe raiz menor que 0')
        resultado = numero1 **  (1 / numero2)
        mostrar = f'A raiz {numero2} de {numero1}é igual a {resultado}'
        gera_historico(mostrar)

def resto_da_divisão():
        cabeçalho('RAIZ')
        numero1 = leiaFloat('Digite a dividendo: ')
        numero2 = leiaFloat('Digite o divisor: ')
        try:
            resultado = numero1 % numero2
        except ZeroDivisionError:
            print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'O resto de {numero1} dividido por  {numero2} é igual a {resultado}'
            gera_historico(mostrar)

def divisão_inteira():
        cabeçalho('DIVISÃO INTEIRA')
        numero1 = leiaFloat('Digite o primeiro número: ')
        numero2 = leiaFloat('Digite um número para dividir o primeiro: ')
        try:
            resultado = numero1 // numero2
        except ZeroDivisionError:
             print('Não é possível dividir um número por zero.')
        else:
            mostrar = f'A divisão inteira entre {numero1} e {numero2} deu {resultado}'
            gera_historico(mostrar)

def funcao_historico():
    cabeçalho('HISTÓRICO')
    contador = 1
    for operacao in historico:
        print(f'\033[33m{contador}\033[m - \033[34m{operacao}\033[m')
        contador += 1
    print(linha())

historico = []
cabeçalho('CALCULADORA')
while True:
    resposta_menu = menu(['Sair', 'Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Potência', 
                     'Raiz quadrada', 'Resto da divisão', 'Divisão inteira',
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
         resto_da_divisão()
    elif resposta_menu == 8:
         divisão_inteira()
    elif resposta_menu == 9:
        funcao_historico()
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
    