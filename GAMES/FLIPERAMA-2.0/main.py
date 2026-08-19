from time import sleep

from carteira import (
    depositar,
    sacar,
    mostrar_extrato,
    validar_aposta,
    atualizar_aposta
)

from conquistas import controlar_conquistas

from jogador import ficha_do_jogador

from perfil import (
    mostrar_perfil,
    ver_estatisticas_dos_jogos,
    ver_conquistas
)

from utilidades import cabeçalho, menu

from loja import (
    listar_cores_de_fundo,
    listar_cores_de_fonte,
    listar_emojis,
    comprar_cor_de_fonte,
    comprar_cor_de_fundo,
    comprar_emoji
)

from jogos import (
    jokenpo,
    par_ou_impar,
    advinhe_o_numero,
    corrida,
    blackjack,
    dados
)

from jogos.jogo_da_forca_pasta import jogo_da_forca_arquivo
from jogos.jogo_da_velha_pasta import jogo_da_velha_arquivo


# ==========================================================
# CONFIGURAÇÃO DOS JOGOS
# ==========================================================

JOGOS = {
    1: (
        'JOKENPÔ',
        jokenpo.jokenpo,
        'jokenpo'
    ),

    2: (
        'PAR OU ÍMPAR',
        par_ou_impar.par_ou_impar,
        'par_ou_impar'
    ),

    3: (
        'ADIVINHE O NÚMERO',
        advinhe_o_numero.adivinhe_o_numero,
        'adivinhe_o_numero'
    ),

    4: (
        'CORRIDA DE CAVALOS',
        corrida.corrida_de_cavalos,
        'corrida_de_cavalos'
    ),

    5: (
        'BLACKJACK',
        blackjack.blackjack_21,
        'blackjack'
    ),

    6: (
        'DADOS',
        dados.jogo_de_dados,
        'jogo-de-dados'
    ),

    7: (
        'JOGO DA FORCA',
        jogo_da_forca_arquivo.jogo_da_forca_funcao,
        'jogo-da-forca'
    ),

    8: (
        'JOGO DA VELHA',
        jogo_da_velha_arquivo.jogo_da_velha_funcao,
        'jogo-da-velha'
    )
}


# ==========================================================
# GERENCIAMENTO DE PARTIDA
# ==========================================================

def gerencia_partida(nome, jogo, estatistica):
    """
    Controla tudo que acontece antes e depois de uma partida.
    """

    cabeçalho(nome)

    saldo = ficha_do_jogador['carteira']['saldo']

    aposta = validar_aposta(saldo)

    if aposta is None:
        print('Não foi possível realizar a aposta.')
        sleep(1)
        return

    # Retira a aposta da carteira
    ficha_do_jogador['carteira']['saldo'] -= aposta

    ficha_do_jogador['extrato'].append(
        (f'Aposta {estatistica}', -aposta)
    )

    # Executa o jogo
    resultado = jogo()

    # Atualiza estatísticas
    ficha_do_jogador['estatisticas_gerais']['partidas_totais'] += 1

    ficha_do_jogador['estatisticas_jogos'][estatistica]['partidas'] += 1

    # Processa o resultado financeiro
    atualizar_aposta(
        ficha_do_jogador,
        aposta,
        resultado,
        estatistica
    )

    # Verifica novas conquistas
    controlar_conquistas(ficha_do_jogador)

    sleep(2)


# ==========================================================
# MENU DE JOGOS
# ==========================================================

def menu_jogos():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'JOKENPÔ',
                'PAR OU ÍMPAR',
                'ADIVINHE O NÚMERO',
                'CORRIDA DE CAVALOS',
                'BLACKJACK',
                'DADOS',
                'JOGO DA FORCA',
                'JOGO DA VELHA'
            ],
            menu_titulo='JOGOS'
        )

        if escolha == 0:
            cabeçalho('VOLTANDO')
            break

        jogo = JOGOS.get(escolha)

        if jogo is None:
            continue

        nome, funcao, estatistica = jogo

        gerencia_partida(
            nome,
            funcao,
            estatistica
        )


# ==========================================================
# MENU DE PERFIL
# ==========================================================

def menu_perfil():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'VER PERFIL GERAL',
                'VER ESTATÍSTICAS DOS JOGOS',
                'VER CONQUISTAS'
            ],
            menu_titulo='PERFIL'
        )

        if escolha == 0:
            cabeçalho('VOLTANDO')
            break

        elif escolha == 1:
            cabeçalho('PERFIL')
            mostrar_perfil(ficha_do_jogador)

        elif escolha == 2:
            cabeçalho('ESTATÍSTICAS DOS JOGOS')
            ver_estatisticas_dos_jogos(ficha_do_jogador)

        elif escolha == 3:
            cabeçalho('CONQUISTAS')
            ver_conquistas(ficha_do_jogador)


# ==========================================================
# MENU DA CARTEIRA
# ==========================================================

def menu_carteira():

    while True:

        cabeçalho('CARTEIRA')

        print(
            f'Saldo atual: '
            f'R${ficha_do_jogador["carteira"]["saldo"]:.2f}'
        )

        escolha = menu(
            lista=[
                'VOLTAR',
                'DEPOSITAR',
                'SACAR',
                'EXTRATO'
            ],
            menu_titulo='CARTEIRA'
        )

        if escolha == 0:
            cabeçalho('VOLTANDO')
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

            cabeçalho('EXTRATO')

            mostrar_extrato(
                ficha_do_jogador['extrato'],
                ficha_do_jogador['carteira']['saldo']
            )


# ==========================================================
# LOJA
# ==========================================================

def menu_cores_fundo():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'LISTAR CORES DE FUNDO',
                'COMPRAR CORES DE FUNDO'
            ],
            menu_titulo='COR DE FUNDO'
        )

        if escolha == 0:
            break

        elif escolha == 1:
            cabeçalho('CORES DE FUNDO')
            listar_cores_de_fundo()

        elif escolha == 2:
            cabeçalho('COMPRAR COR DE FUNDO')
            comprar_cor_de_fundo(ficha_do_jogador)


def menu_cores_fonte():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'LISTAR CORES DE FONTE',
                'COMPRAR CORES DE FONTE'
            ],
            menu_titulo='COR DE FONTE'
        )

        if escolha == 0:
            break

        elif escolha == 1:
            cabeçalho('CORES DE FONTE')
            listar_cores_de_fonte()

        elif escolha == 2:
            cabeçalho('COMPRAR COR DE FONTE')
            comprar_cor_de_fonte(ficha_do_jogador)


def menu_emojis():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'LISTAR EMOJIS',
                'COMPRAR EMOJIS'
            ],
            menu_titulo='EMOJIS'
        )

        if escolha == 0:
            break

        elif escolha == 1:
            cabeçalho('EMOJIS')
            listar_emojis()

        elif escolha == 2:
            cabeçalho('COMPRAR EMOJIS')
            comprar_emoji()


def menu_loja():

    while True:

        escolha = menu(
            lista=[
                'VOLTAR',
                'COR DE FUNDO',
                'COR DE FONTE',
                'EMOJI'
            ],
            menu_titulo='LOJA'
        )

        if escolha == 0:
            cabeçalho('VOLTANDO')
            break

        elif escolha == 1:
            menu_cores_fundo()

        elif escolha == 2:
            menu_cores_fonte()

        elif escolha == 3:
            menu_emojis()


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

def menu_principal():

    while True:

        escolha = menu(
            lista=[
                'SAIR',
                'JOGAR',
                'PERFIL',
                'CARTEIRA',
                'LOJA'
            ],
            menu_titulo='FLIPERAMA DO VICTOR'
        )

        if escolha == 0:

            cabeçalho('SAINDO')

            print('Obrigado por jogar!')
            break

        elif escolha == 1:
            cabeçalho('JOGAR')
            menu_jogos()

        elif escolha == 2:
            menu_perfil()

        elif escolha == 3:
            menu_carteira()

        elif escolha == 4:
            menu_loja()


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == '__main__':
    menu_principal()