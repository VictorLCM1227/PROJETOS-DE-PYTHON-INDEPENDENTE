# loja


def listar_cores_de_fundo():
    contador = 0
    print('===== CORES DE FUNDO =====')
    for cor, informacoes in cores_de_fundo.items():
        print(f'[{contador}] {cor} - R${informacoes["preco"]}')
        contador += 1

def listar_cores_de_fonte():
    contador = 0
    print('===== CORES DE FONTE =====')
    for cor, informacoes in cores_de_fonte.items():
        print(f'[{contador}] {cor} - R${informacoes["preco"]}')
        contador += 1
        

def listar_emojis():
    contador = 0
    print('===== EMOJIS =====')
    for emoji, informacoes in emojis.items():
        print(f'[{contador}] {emoji} - R${informacoes["preco"]}')
        contador += 1

cores_de_fundo = {
    'Preto': {
        'id': 'fundo_preto',
        'codigo_ansi': '\033[1;40m',
        'preco': 100
    },

    'Vermelho': {
        'id': 'fundo_vermelho',
        'codigo_ansi': '\033[1;41m',
        'preco': 100
    },

    'Verde': {
        'id': 'fundo_verde',
        'codigo_ansi': '\033[1;42m',
        'preco': 100
    },

    'Amarelo': {
        'id': 'fundo_amarelo',
        'codigo_ansi': '\033[1;43m',
        'preco': 100
    },

    'Azul': {
        'id': 'fundo_azul',
        'codigo_ansi': '\033[1;44m',
        'preco': 100
    },

    'Magenta': {
        'id': 'fundo_magenta',
        'codigo_ansi': '\033[1;45m',
        'preco': 100
    },

    'Cyan': {
        'id': 'fundo_cyan',
        'codigo_ansi': '\033[1;46m',
        'preco': 100
    },

    'Cinza Claro': {
        'id': 'fundo_cinza_claro',
        'codigo_ansi': '\033[1;47m',
        'preco': 100
    },

    'Cinza Escuro': {
        'id': 'fundo_cinza_escuro',
        'codigo_ansi': '\033[1;100m',
        'preco': 100
    },

    'Vermelho Claro': {
        'id': 'fundo_vermelho_claro',
        'codigo_ansi': '\033[1;101m',
        'preco': 100
    },

    'Verde Claro': {
        'id': 'fundo_verde_claro',
        'codigo_ansi': '\033[1;102m',
        'preco': 100
    },

    'Amarelo Claro': {
        'id': 'fundo_amarelo_claro',
        'codigo_ansi': '\033[1;103m',
        'preco': 100
    },

    'Azul Claro': {
        'id': 'fundo_azul_claro',
        'codigo_ansi': '\033[1;104m',
        'preco': 100
    },

    'Magenta Claro': {
        'id': 'fundo_magenta_claro',
        'codigo_ansi': '\033[1;105m',
        'preco': 100
    },

    'Cyan Claro': {
        'id': 'fundo_cyan_claro',
        'codigo_ansi': '\033[1;106m',
        'preco': 100
    },

    'Branco': {
        'id': 'fundo_branco',
        'codigo_ansi': '\033[1;107m',
        'preco': 100
    },
}

cores_de_fonte = {
    'Preto': {
        'id': 'fonte_preto',
        'codigo_ansi': '\033[1;30m',
        'preco': 100
    },

    'Vermelho': {
        'id': 'fonte_vermelho',
        'codigo_ansi': '\033[1;31m',
        'preco': 100
    },

    'Verde': {
        'id': 'fonte_verde',
        'codigo_ansi': '\033[1;32m',
        'preco': 100
    },

    'Amarelo': {
        'id': 'fonte_amarelo',
        'codigo_ansi': '\033[1;33m',
        'preco': 100
    },

    'Azul': {
        'id': 'fonte_azul',
        'codigo_ansi': '\033[1;34m',
        'preco': 100
    },

    'Magenta': {
        'id': 'fonte_magenta',
        'codigo_ansi': '\033[1;35m',
        'preco': 100
    },

    'Cyan': {
        'id': 'fonte_cyan',
        'codigo_ansi': '\033[1;36m',
        'preco': 100
    },

    'Cinza Claro': {
        'id': 'fonte_cinza_claro',
        'codigo_ansi': '\033[1;37m',
        'preco': 100
    },

    'Cinza Escuro': {
        'id': 'fonte_cinza_escuro',
        'codigo_ansi': '\033[1;90m',
        'preco': 100
    },

    'Vermelho Claro': {
        'id': 'fonte_vermelho_claro',
        'codigo_ansi': '\033[1;91m',
        'preco': 100
    },

    'Verde Claro': {
        'id': 'fonte_verde_claro',
        'codigo_ansi': '\033[1;92m',
        'preco': 100
    },

    'Amarelo Claro': {
        'id': 'fonte_amarelo_claro',
        'codigo_ansi': '\033[1;93m',
        'preco': 100
    },

    'Azul Claro': {
        'id': 'fonte_azul_claro',
        'codigo_ansi': '\033[1;94m',
        'preco': 100
    },

    'Magenta Claro': {
        'id': 'fonte_magenta_claro',
        'codigo_ansi': '\033[1;95m',
        'preco': 100
    },

    'Cyan Claro': {
        'id': 'fonte_cyan_claro',
        'codigo_ansi': '\033[1;96m',
        'preco': 100
    },
}


emojis = {
    'Coração': {
        'id': 'emoji_coracao',
        'emoji': '❤️',
        'preco': 100
    },

    'Fogo': {
        'id': 'emoji_fogo',
        'emoji': '🔥',
        'preco': 100
    },

    'Coroa': {
        'id': 'emoji_coroa',
        'emoji': '👑',
        'preco': 100
    },

    'Estrela': {
        'id': 'emoji_estrela',
        'emoji': '⭐',
        'preco': 100
    },

    'Diamante': {
        'id': 'emoji_diamante',
        'emoji': '💎',
        'preco': 100
    },

    'Trofeu': {
        'id': 'emoji_trofeu',
        'emoji': '🏆',
        'preco': 100
    },

    'Dinheiro': {
        'id': 'emoji_dinheiro',
        'emoji': '💰',
        'preco': 100
    },

    'Raio': {
        'id': 'emoji_raio',
        'emoji': '⚡',
        'preco': 100
    },

    'Cereja': {
        'id': 'emoji_cereja',
        'emoji': '🍒',
        'preco': 100
    },

    'Cadeado': {
        'id': 'emoji_cadeado',
        'emoji': '🔒',
        'preco': 100
    },

    'Foguete': {
        'id': 'emoji_foguete',
        'emoji': '🚀',
        'preco': 100
    },

    'Caveira': {
        'id': 'emoji_caveira',
        'emoji': '💀',
        'preco': 100
    },

    'Fantasma': {
        'id': 'emoji_fantasma',
        'emoji': '👻',
        'preco': 100
    },

    'Robô': {
        'id': 'emoji_robo',
        'emoji': '🤖',
        'preco': 100
    },

    'Alienígena': {
        'id': 'emoji_alienigena',
        'emoji': '👽',
        'preco': 100
    },

    'Óculos': {
        'id': 'emoji_oculos',
        'emoji': '😎',
        'preco': 100
    },

    'Raiva': {
        'id': 'emoji_raiva',
        'emoji': '😡',
        'preco': 100
    },

    'Riso': {
        'id': 'emoji_riso',
        'emoji': '😂',
        'preco': 100
    },

    'Palhaço': {
        'id': 'emoji_palhaco',
        'emoji': '🤡',
        'preco': 100
    },

    'Cavalo': {
        'id': 'emoji_cavalo',
        'emoji': '🐎',
        'preco': 100
    },
}


reset = '\033[0;0m'
jogador_fonte = '\033[1;97m'  # branco
jogador_fundo = '\033[1;97m'  # branco