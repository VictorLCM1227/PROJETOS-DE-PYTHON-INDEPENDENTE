
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
    while True:
        opcao = int(input('>>> O que deseja fazer? '))
        if opcao in (0, 1, 2, 3, 4):
            break
        print('Opção inváliida. Somente 0, 1, 2, 3 ou 4.')
    if opcao == 0:
        print('Saindo...')
        break

    elif opcao == 1:
        print('Consultando Saldo...')
        sleep(0.5)
        print(f'Seu Saldo é de R${saldo}')

    elif opcao == 2:
        deposito = int(input('Valor do depósito: R$'))
        if deposito < 1:
            print('O valor do depósito deve ser maior que zero.')
        else:
            print('Depositando...')
            sleep(0.5)
            saldo += deposito
            extrato.append(deposito)

    elif opcao == 3:
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

    elif opcao == 4:
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
    print('-' * 30)
print('=' * 30)
print('Volte sempre ao BANCO VICTOR! Tenha um ótimo dia.')