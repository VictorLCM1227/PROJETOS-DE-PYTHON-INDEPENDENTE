# corrida_de_cavalos.py

from random import randint
from time import sleep

from utilidades import cabeçalho, linha, menu_corrida


LINHA_DE_CHEGADA = 35

CAVALOS = {
    'Cadillac': {
        'velocidade': 5,
        'sorte': 3
    },

    'Princesa': {
        'velocidade': 7,
        'sorte': 3
    }
}


def corrida_de_cavalos():

    cabeçalho('CORRIDA DE CAVALOS')

    cavalos = {
        nome: {
            'velocidade': dados['velocidade'],
            'sorte': dados['sorte'],
            'posicao': 0
        }

        for nome, dados in CAVALOS.items()
    }

    nomes = list(cavalos)

    while True:

        aposta = menu_corrida(cavalos)

        if 0 <= aposta < len(nomes):
            break

        print(
            f'Opção inválida! '
            f'Escolha um cavalo de 0 a {len(nomes) - 1}.'
        )

    cavalo_apostado = nomes[aposta]

    vencedor = executar_corrida(cavalos, nomes)

    print()

    if vencedor == cavalo_apostado:

        print('VOCÊ VENCEU A APOSTA!')

        return 'vitoria'

    if vencedor == 'empate':

        print('A corrida terminou empatada.')

        return 'empate'

    print('VOCÊ PERDEU A APOSTA!')

    return 'derrota'


def executar_corrida(cavalos, nomes):

    corrida_terminou = False

    while not corrida_terminou:

        for nome in nomes:

            cavalos[nome]['posicao'] += randint(
                1,
                cavalos[nome]['velocidade']
            )

            cavalos[nome]['posicao'] = min(
                cavalos[nome]['posicao'],
                LINHA_DE_CHEGADA
            )

        mostrar_corrida(cavalos, nomes)

        sleep(1)

        for nome in nomes:

            if cavalos[nome]['posicao'] >= LINHA_DE_CHEGADA:
                corrida_terminou = True
                break

    return verificar_vencedor(cavalos, nomes)


def mostrar_corrida(cavalos, nomes):

    for nome in nomes:

        posicao = cavalos[nome]['posicao']

        pista = (
            ' ' * (posicao - 1)
            + '🐎'
            + ' ' * (LINHA_DE_CHEGADA - posicao)
            + '|🏁'
        )

        print(f'{nome:8}: {pista}')

    print(linha())


def verificar_vencedor(cavalos, nomes):

    posicoes = [
        cavalos[nome]['posicao']
        for nome in nomes
    ]

    maior_posicao = max(posicoes)

    vencedores = [
        nome
        for nome in nomes
        if cavalos[nome]['posicao'] == maior_posicao
    ]

    if len(vencedores) > 1:

        print('HOUVE EMPATE! CORRIDA ANULADA!')

        return 'empate'

    vencedor = vencedores[0]

    print(
        f'O CAVALO {vencedor} '
        f'VENCEU A CORRIDA!'
    )

    return vencedor