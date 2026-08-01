#carteira

from utilidades import leiaInt, linha, cabeçalho, menu, leiaFloatPositivo
from time import sleep

def depositar(saldo, extrato):
    while True:
        deposito = int(input('Valor do depósito: R$'))
        if deposito < 1:
            print('O valor do depósito deve ser maior que zero.')
        else:
            print('Depositando...')
            sleep(0.5)
            saldo += deposito
            extrato.append(deposito)
            return saldo, extrato

def sacar(saldo, extrato):
    while True:
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
                return saldo, extrato

def mostrar_extrato(extrato):
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

def pagar_para_jogar(custo, saldo, extrato):
    if custo < saldo:
        print('Você não tem dinheiro para jogar esse jogo.')
    else:
        saldo - custo
        extrato.append(custo)
        return saldo, extrato

#se o saldo for insuficiente, a função retorna none
def validar_aposta(saldo):
    if saldo <= 0:
        print('Saldo insuficiente.')
    else:
        while True:
            aposta = leiaFloatPositivo('Quanto deseja apostar? R$')
            if aposta <= saldo:
                return aposta
            print('A sua aposta só pode ser menor ou igual ao seu saldo.')
        