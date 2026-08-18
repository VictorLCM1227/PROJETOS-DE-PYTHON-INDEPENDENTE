# jogador.py

def criar_carteira():
    return {
        'saldo': 0.0
    }


def criar_estatisticas_gerais():
    return {
        'partidas_totais': 0,
        'vitorias_totais': 0,
        'derrotas_totais': 0,
        'empates_totais': 0,
        'dinheiro_ganho': 0.0,
        'dinheiro_perdido': 0.0
    }


def criar_estatisticas_jogos():
    return {
        'jokenpo': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0,
            'empates': 0
        },

        'par_ou_impar': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0,
            'empates': 0
        },

        'adivinhe_o_numero': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0
        },

        'corrida_de_cavalos': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0
        },

        'blackjack': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0,
            'empates': 0
        },

        'jogo-de-dados': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0
        },

        'jogo-da-forca': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0
        },

        'jogo-da-velha': {
            'partidas': 0,
            'vitorias': 0,
            'derrotas': 0,
            'empates': 0
        }
    }


def criar_inventario():
    return {
        'cores_fundo': [],
        'cores_fonte': [],
        'emojis': []
    }


def criar_equipamentos():
    return {
        'cor_fundo': None,
        'cor_fonte': None,
        'emoji': None
    }


def criar_conquistas():
    return {
        'primeira_partida': False,
        'primeira_vitoria': False,
        'dez_vitorias': False,
        'cinquenta_partidas': False,
        'grande_ganhador': False
    }


def criar_ficha(nome):

    return {
        'nome': nome,

        'carteira': criar_carteira(),

        'extrato': [],

        'estatisticas_gerais': criar_estatisticas_gerais(),

        'estatisticas_jogos': criar_estatisticas_jogos(),

        'conquistas': criar_conquistas(),

        'inventario': criar_inventario(),

        'equipado': criar_equipamentos()
    }