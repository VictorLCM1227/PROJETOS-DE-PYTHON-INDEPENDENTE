from time import sleep

pontos = 0

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

def linha(simbolo='-', tam=42):
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

def verificar_tamanho():
    global senha, pontos
    tamanho = len(senha)
    print(f'Possui 8 ou mais caracteres: ', end='')
    if tamanho >= 8:
        pontos += 1
        print('SIM')
    else:
        print('NÃO')


def verificar_maiuscula():
    nao = True
    global senha, pontos
    print(f'Possui letras maiúsculas: ', end='')
    for letra in senha:
        if letra.isupper():
            print('SIM')
            nao = False
            pontos += 1
            break
    if nao:
        print('NÃO')
            

def verificar_minuscula():
    nao = True
    global senha, pontos
    print(f'Possui letras minúsculas: ', end='')
    for letra in senha:
        if letra.islower():
            print('SIM')
            nao = False
            pontos += 1
            break
    if nao:
        print('NÃO')
            
def verificar_numero():
    nao = True
    global senha, pontos
    print(f'Possui números: ', end='')
    for letra in senha:
        if letra.isnumeric():
            print('SIM')
            nao = False
            pontos += 1
            break
    if nao:
        print('NÃO')

def verificar_especial():
    nao = True
    global senha, pontos
    print(f'Possui caracteres especiais: ', end='')
    for letra in senha:
        if not letra.isalnum():
            print('SIM')
            nao = False
            pontos += 1
            break
    if nao:
        print('NÃO')

def calcular_forca():
    global senha, pontos
    if pontos == 5:
        senha_nivel = 'FORTE'
    elif pontos >= 3:
        senha_nivel = 'MÉDIA'
    elif pontos < 3:
        senha_nivel = 'FRACA'
    print(f'Senha {senha_nivel}')

cabecalho('VERIFICADOR DE SENHA', simbolo='=')
senha = input('Digite sua senha: ')
print('Analisando...')
sleep(0.5)

verificar_tamanho()
verificar_maiuscula()
verificar_minuscula()
verificar_numero()
verificar_especial()
calcular_forca()