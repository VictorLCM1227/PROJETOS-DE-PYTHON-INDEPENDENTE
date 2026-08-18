from utilidades import cabeçalho, menu, leia_float


def depositar(saldo, extrato):

    cabeçalho('DEPÓSITO')

    valor = leia_float(
        'Valor para depositar: R$ ',
        minimo=0.01
    )

    saldo += valor

    extrato.append({
        'tipo': 'Depósito',
        'valor': valor,
        'saldo': saldo
    })

    print(f'\nDepósito de R$ {valor:.2f} realizado.')
    print(f'Novo saldo: R$ {saldo:.2f}')

    return saldo, extrato


def sacar(saldo, extrato):

    cabeçalho('SAQUE')

    valor = leia_float(
        'Valor para sacar: R$ ',
        minimo=0.01
    )

    if valor > saldo:
        print('\nERRO: saldo insuficiente.')
        return saldo, extrato

    saldo -= valor

    extrato.append({
        'tipo': 'Saque',
        'valor': -valor,
        'saldo': saldo
    })

    print(f'\nSaque de R$ {valor:.2f} realizado.')
    print(f'Novo saldo: R$ {saldo:.2f}')

    return saldo, extrato


def validar_aposta(saldo):

    valor = leia_float(
        'Valor da aposta: R$ ',
        minimo=0.01
    )

    if valor > saldo:
        print('\nERRO: saldo insuficiente.')
        return None

    return valor


def atualizar_aposta(
    saldo,
    extrato,
    aposta,
    resultado
):

    if resultado == 'vitoria':

        premio = aposta * 2
        saldo += premio

        extrato.append({
            'tipo': 'Vitória',
            'valor': premio,
            'saldo': saldo
        })

        print(f'\nVocê ganhou R$ {premio:.2f}!')

    elif resultado == 'derrota':

        saldo -= aposta

        extrato.append({
            'tipo': 'Derrota',
            'valor': -aposta,
            'saldo': saldo
        })

        print(f'\nVocê perdeu R$ {aposta:.2f}.')

    elif resultado == 'empate':

        extrato.append({
            'tipo': 'Empate',
            'valor': 0,
            'saldo': saldo
        })

        print('\nAposta devolvida.')

    return saldo, extrato


def mostrar_extrato(extrato, saldo):

    cabeçalho('EXTRATO')

    if not extrato:
        print('Nenhuma movimentação encontrada.')
        return

    for movimento in extrato:

        tipo = movimento['tipo']
        valor = movimento['valor']
        saldo_movimento = movimento['saldo']

        sinal = '+' if valor > 0 else ''

        print(
            f'{tipo:<15} '
            f'{sinal}R$ {valor:.2f} '
            f'| Saldo: R$ {saldo_movimento:.2f}'
        )

    print('-' * 50)
    print(f'SALDO ATUAL: R$ {saldo:.2f}')


def menu_carteira(ficha_do_jogador):

    while True:

        saldo = ficha_do_jogador['carteira']['saldo']

        escolha = menu(
            lista=[
                'VOLTAR',
                'DEPOSITAR',
                'SACAR',
                'EXTRATO'
            ],
            menu_titulo=f'CARTEIRA | R$ {saldo:.2f}'
        )

        if escolha == 0:
            break

        elif escolha == 1:

            (
                ficha_do_jogador['carteira']['saldo'],
                ficha_do_jogador['extrato']
            ) = depositar(
                ficha_do_jogador['carteira']['saldo'],
                ficha_do_jogador['extrato']
            )

        elif escolha == 2:

            (
                ficha_do_jogador['carteira']['saldo'],
                ficha_do_jogador['extrato']
            ) = sacar(
                ficha_do_jogador['carteira']['saldo'],
                ficha_do_jogador['extrato']
            )

        elif escolha == 3:

            mostrar_extrato(
                ficha_do_jogador['extrato'],
                ficha_do_jogador['carteira']['saldo']
            )