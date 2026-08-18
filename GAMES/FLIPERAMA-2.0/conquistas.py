# conquistas.py

from utilidades import cabeçalho, menu


CONQUISTAS = {
    'primeira_partida': {
        'nome': 'Primeiro Passo',
        'descricao': 'Jogue sua primeira partida.',
        'criterio': 'partidas_totais',
        'valor': 1
    },

    'primeira_vitoria': {
        'nome': 'Primeira Vitória',
        'descricao': 'Vença sua primeira partida.',
        'criterio': 'vitorias_totais',
        'valor': 1
    },

    'dez_vitorias': {
        'nome': 'Veterano',
        'descricao': 'Consiga 10 vitórias.',
        'criterio': 'vitorias_totais',
        'valor': 10
    },

    'cinquenta_partidas': {
        'nome': 'Jogador Dedicado',
        'descricao': 'Jogue 50 partidas.',
        'criterio': 'partidas_totais',
        'valor': 50
    },

    'grande_ganhador': {
        'nome': 'Grande Ganhador',
        'descricao': 'Acumule R$ 1.000 em ganhos.',
        'criterio': 'dinheiro_ganho',
        'valor': 1000
    }
}


def desbloquear_conquista(ficha_do_jogador, codigo):

    if ficha_do_jogador['conquistas'].get(codigo, False):
        return False

    ficha_do_jogador['conquistas'][codigo] = True

    conquista = CONQUISTAS[codigo]

    cabeçalho('CONQUISTA DESBLOQUEADA!')

    print(f'🏆 {conquista["nome"]}')
    print(conquista['descricao'])

    return True


def verificar_conquista(ficha_do_jogador, codigo):

    conquista = CONQUISTAS[codigo]

    criterio = conquista['criterio']
    valor_necessario = conquista['valor']

    valor_atual = ficha_do_jogador[
        'estatisticas_gerais'
    ].get(criterio, 0)

    return valor_atual >= valor_necessario


def controlar_conquistas(ficha_do_jogador):

    for codigo in CONQUISTAS:

        if ficha_do_jogador['conquistas'].get(codigo, False):
            continue

        if verificar_conquista(
            ficha_do_jogador,
            codigo
        ):
            desbloquear_conquista(
                ficha_do_jogador,
                codigo
            )


def ver_conquistas(ficha_do_jogador):

    cabeçalho('CONQUISTAS')

    total = len(CONQUISTAS)
    desbloqueadas = 0

    for codigo, conquista in CONQUISTAS.items():

        desbloqueada = ficha_do_jogador[
            'conquistas'
        ].get(codigo, False)

        if desbloqueada:
            simbolo = '[X]'
            desbloqueadas += 1
        else:
            simbolo = '[ ]'

        print(f'\n{simbolo} {conquista["nome"]}')
        print(f'    {conquista["descricao"]}')

    print(
        f'\nProgresso: '
        f'{desbloqueadas}/{total}'
    )


def menu_conquistas(ficha_do_jogador):

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'VER CONQUISTAS'
            ],
            menu_titulo='CONQUISTAS'
        )

        if escolha == 0:
            break

        elif escolha == 1:
            ver_conquistas(ficha_do_jogador)