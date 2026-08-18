from utilidades import cabeçalho, menu


def mostrar_configuracoes(ficha_do_jogador):

    cabeçalho('CONFIGURAÇÕES')

    equipado = ficha_do_jogador['equipado']

    print(f'Cor de fundo: {equipado["cor_fundo"]}')
    print(f'Cor da fonte: {equipado["cor_fonte"]}')
    print(f'Emoji: {equipado["emoji"]}')


def alterar_cor_fundo(ficha_do_jogador):

    inventario = ficha_do_jogador['inventario']['cores_fundo']

    if not inventario:
        print('Você não possui cores de fundo.')
        return

    cabeçalho('COR DE FUNDO')

    for numero, cor in enumerate(inventario, 1):
        print(f'{numero} - {cor}')

    while True:

        try:
            escolha = int(input('\nEscolha a cor: '))

            if 1 <= escolha <= len(inventario):
                cor = inventario[escolha - 1]

                ficha_do_jogador['equipado']['cor_fundo'] = cor

                print(f'\nCor de fundo equipada: {cor}')
                break

            print('ERRO: opção inválida.')

        except ValueError:
            print('ERRO: digite um número válido.')


def alterar_cor_fonte(ficha_do_jogador):

    inventario = ficha_do_jogador['inventario']['cores_fonte']

    if not inventario:
        print('Você não possui cores de fonte.')
        return

    cabeçalho('COR DE FONTE')

    for numero, cor in enumerate(inventario, 1):
        print(f'{numero} - {cor}')

    while True:

        try:
            escolha = int(input('\nEscolha a cor: '))

            if 1 <= escolha <= len(inventario):
                cor = inventario[escolha - 1]

                ficha_do_jogador['equipado']['cor_fonte'] = cor

                print(f'\nCor de fonte equipada: {cor}')
                break

            print('ERRO: opção inválida.')

        except ValueError:
            print('ERRO: digite um número válido.')


def alterar_emoji(ficha_do_jogador):

    inventario = ficha_do_jogador['inventario']['emojis']

    if not inventario:
        print('Você não possui emojis.')
        return

    cabeçalho('EMOJI')

    for numero, emoji in enumerate(inventario, 1):
        print(f'{numero} - {emoji}')

    while True:

        try:
            escolha = int(input('\nEscolha o emoji: '))

            if 1 <= escolha <= len(inventario):
                emoji = inventario[escolha - 1]

                ficha_do_jogador['equipado']['emoji'] = emoji

                print(f'\nEmoji equipado: {emoji}')
                break

            print('ERRO: opção inválida.')

        except ValueError:
            print('ERRO: digite um número válido.')


def menu_configuracoes(ficha_do_jogador):

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'COR DE FUNDO',
                'COR DE FONTE',
                'EMOJI',
                'VER CONFIGURAÇÕES'
            ],
            menu_titulo='CONFIGURAÇÕES'
        )

        if escolha == 0:
            break

        elif escolha == 1:
            alterar_cor_fundo(ficha_do_jogador)

        elif escolha == 2:
            alterar_cor_fonte(ficha_do_jogador)

        elif escolha == 3:
            alterar_emoji(ficha_do_jogador)

        elif escolha == 4:
            mostrar_configuracoes(ficha_do_jogador)