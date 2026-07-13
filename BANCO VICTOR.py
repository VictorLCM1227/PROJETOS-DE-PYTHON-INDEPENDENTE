
from time import sleep
extrato = []
saldo = 0
print('=' * 30)
print(f'{" BANCO VICTOR ":^30}')
print('=' * 30)
while True:
    print('''[0] Para sair
[1] Consultar saldo
[2] Depositar dinheiro
[3] Sacar dinheiro
[4] Mostrar o extrato''')
    print('-' * 30)
    opcao = int(input('>>> O que deseja fazer? '))
    if opcao == 0:
        print('Saindo...')
        break
    elif opcao == 1:
        print('Consultando Saldo...')
        sleep(1)
        print(f'Seu Saldo é de R${saldo}')
    elif opcao == 2:
        deposito = int(input('Valor do depósito: R$'))
        saldo += deposito
    elif opcao == 3:
        saque = int(input('Valor do Saque: R$'))
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
    elif opcao == 4:
        print('Extrato:')
    print('-' * 30)
print('=' * 30)
print('Volte sempre ao BANCO VICTOR! Tenha um ótimo dia.')