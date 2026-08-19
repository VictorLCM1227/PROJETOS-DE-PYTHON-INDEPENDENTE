# loja.py

from utilidades import cabeçalho, leiaIntPositivo, menu


# ============================================================
# CATÁLOGOS DA LOJA
# ============================================================

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
    }
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
    }
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
    }
}


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def _listar_catalogo(catalogo, tipo):
    """
    Mostra todos os itens de um catálogo.
    """

    print(f'===== {tipo.upper()} =====')

    for numero, (nome, item) in enumerate(
        catalogo.items()
    ):
        if 'emoji' in item:
            representacao = item['emoji']

            print(
                f'[{numero}] '
                f'{representacao} '
                f'{nome} - '
                f'R${item["preco"]:.2f}'
            )

        else:
            print(
                f'[{numero}] '
                f'{nome} - '
                f'R${item["preco"]:.2f}'
            )


def _comprar_item(
    ficha_do_jogador,
    catalogo,
    categoria,
    mensagem
):
    """
    Realiza a compra de qualquer item da loja.
    """

    itens = list(catalogo.items())

    while True:

        escolha = leiaIntPositivo(
            'Qual item deseja comprar? '
        )

        if 0 <= escolha < len(itens):
            break

        print('Opção inválida.')

    nome, item = itens[escolha]

    inventario = ficha_do_jogador[
        'inventario'
    ][categoria]

    saldo = ficha_do_jogador[
        'carteira'
    ]['saldo']

    # --------------------------------------------------------
    # Verifica se já possui
    # --------------------------------------------------------

    if item['id'] in inventario:

        print(
            f'Você já possui {nome}.'
        )

        return False

    # --------------------------------------------------------
    # Verifica saldo
    # --------------------------------------------------------

    if saldo < item['preco']:

        print(
            'Saldo insuficiente.'
        )

        print(
            f'Preço: R${item["preco"]:.2f}'
        )

        print(
            f'Saldo: R${saldo:.2f}'
        )

        return False

    # --------------------------------------------------------
    # Compra
    # --------------------------------------------------------

    ficha_do_jogador[
        'carteira'
    ]['saldo'] -= item['preco']

    inventario.append(item['id'])

    ficha_do_jogador[
        'extrato'
    ].append(
        (
            f'{mensagem}: {nome}',
            -item['preco']
        )
    )

    print(
        f'\nCompra realizada!'
    )

    print(
        f'Item: {nome}'
    )

    print(
        f'Valor: R${item["preco"]:.2f}'
    )

    print(
        f'Saldo restante: '
        f'R${ficha_do_jogador["carteira"]["saldo"]:.2f}'
    )

    return True


# ============================================================
# LISTAGEM
# ============================================================

def listar_cores_de_fundo():

    _listar_catalogo(
        cores_de_fundo,
        'CORES DE FUNDO'
    )


def listar_cores_de_fonte():

    _listar_catalogo(
        cores_de_fonte,
        'CORES DE FONTE'
    )


def listar_emojis():

    _listar_catalogo(
        emojis,
        'EMOJIS'
    )


# ============================================================
# COMPRAS
# ============================================================

def comprar_cor_de_fundo(
    ficha_do_jogador
):

    cabeçalho('COMPRAR COR DE FUNDO')

    listar_cores_de_fundo()

    return _comprar_item(
        ficha_do_jogador,
        cores_de_fundo,
        'cores_de_fundo',
        'Compra cor de fundo'
    )


def comprar_cor_de_fonte(
    ficha_do_jogador
):

    cabeçalho('COMPRAR COR DE FONTE')

    listar_cores_de_fonte()

    return _comprar_item(
        ficha_do_jogador,
        cores_de_fonte,
        'cores_de_fonte',
        'Compra cor de fonte'
    )


def comprar_emoji(
    ficha_do_jogador
):

    cabeçalho('COMPRAR EMOJI')

    listar_emojis()

    return _comprar_item(
        ficha_do_jogador,
        emojis,
        'emojis',
        'Compra emoji'
    )


# ============================================================
# INVENTÁRIO
# ============================================================

def mostrar_inventario(
    ficha_do_jogador
):

    inventario = ficha_do_jogador[
        'inventario'
    ]

    cabeçalho('MEU INVENTÁRIO')

    print('CORES DE FUNDO:')

    if inventario['cores_de_fundo']:

        for item_id in inventario[
            'cores_de_fundo'
        ]:

            nome = _nome_por_id(
                cores_de_fundo,
                item_id
            )

            print(f'  - {nome}')

    else:
        print('  Nenhuma.')

    print()

    print('CORES DE FONTE:')

    if inventario['cores_de_fonte']:

        for item_id in inventario[
            'cores_de_fonte'
        ]:

            nome = _nome_por_id(
                cores_de_fonte,
                item_id
            )

            print(f'  - {nome}')

    else:
        print('  Nenhuma.')

    print()

    print('EMOJIS:')

    if inventario['emojis']:

        for item_id in inventario['emojis']:

            nome = _nome_por_id(
                emojis,
                item_id
            )

            item = emojis[nome]

            print(
                f'  - {item["emoji"]} '
                f'{nome}'
            )

    else:
        print('  Nenhum.')


def _nome_por_id(catalogo, item_id):

    for nome, item in catalogo.items():

        if item['id'] == item_id:
            return nome

    return 'Item desconhecido'


# ============================================================
# MENUS
# ============================================================

def menu_cores_de_fundo(
    ficha_do_jogador
):

    while True:

        escolha = menu(
            [
                'VOLTAR',
                'LISTAR CORES',
                'COMPRAR COR'
            ],
            'COR DE FUNDO'
        )

        if escolha == 0:
            break

        elif escolha == 1:

            cabeçalho(
                'CORES DE FUNDO'
            )

            listar_cores_de_fundo()

        elif escolha == 2:

            comprar_cor_de_fundo(
                ficha_do_jogador
            )


def menu_cores_de_fonte(
    ficha_do_jogador
):

    while True:

        escolha = menu(
            [
                'VOLTAR',
                'LISTAR CORES',
                'COMPRAR COR'
            ],
            'COR DE FONTE'
        )

        if escolha == 0:
            break

        elif escolha == 1:

            cabeçalho(
                'CORES DE FONTE'
            )

            listar_cores_de_fonte()

        elif escolha == 2:

            comprar_cor_de_fonte(
                ficha_do_jogador
            )


def menu_emojis(
    ficha_do_jogador
):

    while True:

        escolha = menu(
            [
                'VOLTAR',
                'LISTAR EMOJIS',
                'COMPRAR EMOJI'
            ],
            'EMOJIS'
        )

        if escolha == 0:
            break

        elif escolha == 1:

            cabeçalho(
                'EMOJIS'
            )

            listar_emojis()

        elif escolha == 2:

            comprar_emoji(
                ficha_do_jogador
            )


def menu_loja(
    ficha_do_jogador
):

    while True:

        escolha = menu(
            [
                'VOLTAR',
                'COR DE FUNDO',
                'COR DE FONTE',
                'EMOJIS',
                'MEU INVENTÁRIO'
            ],
            'LOJA'
        )

        if escolha == 0:
            break

        elif escolha == 1:

            menu_cores_de_fundo(
                ficha_do_jogador
            )

        elif escolha == 2:

            menu_cores_de_fonte(
                ficha_do_jogador
            )

        elif escolha == 3:

            menu_emojis(
                ficha_do_jogador
            )

        elif escolha == 4:

            mostrar_inventario(
                ficha_do_jogador
            )