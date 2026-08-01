#carteira

from utilidades import leiaInt, linha, cabeçalho, menu
from time import sleep

extrato = []

def depositar(saldo=0):
    global extrato
    deposito = int(input('Valor do depósito: R$'))
    if deposito < 1:
        print('O valor do depósito deve ser maior que zero.')
    else:
        print('Depositando...')
        sleep(0.5)
        saldo += deposito
        extrato.append(deposito)

def depositar(saldo=0):
    global extrato
    deposito = int(input('Valor do depósito: R$'))
    if deposito < 1:
        print('O valor do depósito deve ser maior que zero.')
    else:
        print('Depositando...')
        sleep(0.5)
        saldo += deposito
        extrato.append(deposito)

def sacar(saldo=0):
    saque = int(input('Valor do Saque: R$'))
    if saque < 1:
        print('O valor do saque deve ser maior que zero.')
    else:
        if saque > saldo:
            print('Saldo Insuficiente.')
        else:
            print('Sacando...')
            sleep(0.5)
            extrato.append(saque * (-1))
            saldo -= saque
            cedula = 200
            cedula_quantidade = 0
            while True:
                if saque >= cedula:
                    saque -= cedula
                    cedula_quantidade += 1
                else:
                    if cedula_quantidade > 0:
                        print(f'Total de {cedula_quantidade} cédulas de R${cedula}')
                    if cedula == 200:
                        cedula = 100
                    elif cedula == 100:
                        cedula = 50
                    elif cedula == 50:
                        cedula = 20
                    elif cedula == 20:
                        cedula = 10
                    elif cedula == 10:
                        cedula = 5
                    elif cedula == 5:
                        cedula = 1
                    cedula_quantidade = 0
                    if saque == 0:
                        break

def mostrar_extrato():
    global extrato
    print('Abrindo extrato:')
    sleep(0.5)
    if not extrato:
        print('Ainda não houve Transações.')
    else:
        for transação in extrato:
            if transação > 0:
                print(f'Depósito de R${abs(transação)}')
            else:
                print(f'Saque de R${abs(transação)}')


def mostrar_saldo(saldo):
    cabeçalho('CARTEIRA')
    print(f'Saldo atual: R${saldo} ')
    escolha_carteira = menu(lista=['VOLTAR', 'DEPOSITAR', 'SACAR', 'EXTRATO'], menu_titulo='')
    if escolha_carteira == 0:
        cabeçalho('VOLTANDO')

    elif escolha_carteira == 1:
        cabeçalho('DEPOSITAR')
        depositar(saldo=saldo)

    elif escolha_carteira == 2:
        cabeçalho('DEPOSITAR')
        sacar(saldo=saldo)

    elif escolha_carteira == 3:
        cabeçalho('EXTRATO')
        mostrar_extrato()