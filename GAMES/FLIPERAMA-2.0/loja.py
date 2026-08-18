# loja.py

from utilidades import cabeçalho, menu


CORES_DE_FUNDO = {
    'azul': {
        'nome': 'Azul',
        'codigo': '\033[44m',
        'preco': 100
    },

    'verde': {
        'nome': 'Verde',
        'codigo': '\033[42m',
        'preco': 100
    },

    'vermelho': {
        'nome': 'Vermelho',
        'codigo': '\033[41m',
        'preco': 100
    }
}


CORES_DE_FONTE = {
    'azul': {
        'nome': 'Azul',
        'codigo': '\033[34m',
        'preco': 50
    },

    'verde': {
        'nome': 'Verde',
        'codigo': '\033[32m',
        'preco': 50
    },

    'amarelo': {
        'nome': 'Amarelo',
        'codigo': '\033[33m',
        'preco': 50
    }
}


EMOJIS = {
    'feliz': {
        'nome': 'Feliz',
        'emoji': '😎',
        'preco': 150
    },

    'fogo': {
        'nome': 'Fogo',
        'emoji': '🔥',
        'preco': 200
    },

    'coroa': {
        'nome': 'Coroa',
        'emoji': '👑',
        'preco': 300
    }
}