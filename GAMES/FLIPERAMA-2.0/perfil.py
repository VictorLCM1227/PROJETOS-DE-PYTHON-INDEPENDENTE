# perfil.py

from utilidades import cabeçalho, menu


def mostrar_perfil(ficha_do_jogador):

    cabeçalho('MEU PERFIL')

    print(f'Nome: {ficha_do_jogador["nome"]}')

    print('\n===== ESTATÍSTICAS GERAIS =====')

    for atributo, valor in ficha_do_jogador['estatisticas_gerais'].items():
        nome_atributo = atributo.replace('_', ' ').title()
        print(f'{nome_atributo}: {valor}')

    partidas = ficha_do_jogador['estatisticas_gerais']['partidas_totais']
    vitorias = ficha_do_jogador['estatisticas_gerais']['vitorias_totais']

    if partidas > 0:
        taxa_de_vitoria = (vitorias / partidas) * 100
    else:
        taxa_de_vitoria = 0

    print(f'Taxa de vitória: {taxa_de_vitoria:.2f}%')

    print('\n===== CARTEIRA =====')

    for atributo, valor in ficha_do_jogador['carteira'].items():
        nome_atributo = atributo.replace('_', ' ').title()

        if atributo == 'saldo':
            print(f'{nome_atributo}: R$ {valor:.2f}')
        else:
            print(f'{nome_atributo}: {valor}')


def ver_estatisticas_dos_jogos(ficha_do_jogador):

    cabeçalho('ESTATÍSTICAS DOS JOGOS')

    for nome, jogo in ficha_do_jogador['estatisticas_jogos'].items():

        print(f'\n===== {nome.replace("_", " ").title()} =====')

        for atributo, valor in jogo.items():
            nome_atributo = atributo.replace('_', ' ').title()

            if 'dinheiro' in atributo:
                print(f'{nome_atributo}: R$ {valor:.2f}')
            else:
                print(f'{nome_atributo}: {valor}')


def ver_conquistas(ficha_do_jogador):

    cabeçalho('CONQUISTAS')

    conquistas = ficha_do_jogador['conquistas']

    desbloqueadas = 0

    for nome, desbloqueada in conquistas.items():

        if desbloqueada:
            simbolo = '[X]'
            desbloqueadas += 1
        else:
            simbolo = '[ ]'

        print(
            f'{simbolo} '
            f'{nome.replace("_", " ").title()}'
        )

    total = len(conquistas)

    print(
        f'\nConquistas: '
        f'{desbloqueadas}/{total}'
    )


def menu_perfil(ficha_do_jogador):

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'PERFIL GERAL',
                'ESTATÍSTICAS DOS JOGOS',
                'CONQUISTAS'
            ],
            menu_titulo='PERFIL'
        )

        if escolha == 0:
            cabeçalho('VOLTANDO')
            break

        elif escolha == 1:
            mostrar_perfil(ficha_do_jogador)

        elif escolha == 2:
            ver_estatisticas_dos_jogos(ficha_do_jogador)

        elif escolha == 3:
            ver_conquistas(ficha_do_jogador)