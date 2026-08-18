from random import choice
from time import sleep

from DADOS import palavras_chave, respostas


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):

    while True:

        try:
            numero = int(input(msg))

        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return numero


def menu(lista):

    cabeçalho('MENU PRINCIPAL')

    for contador, item in enumerate(lista):
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')

    print(linha())

    opcao = leiaInt('\033[32mSua opção: \033[m')

    return opcao


def pergunta_resposta(voce):

    for tema, palavras in palavras_chave.items():

        for palavra in palavras:

            if palavra in voce:
                return tema

    return 'erro'


def responder(categoria):

    return choice(respostas[categoria])


def conversar():

    cabeçalho('CONVERSANDO')

    while True:

        voce = input('\033[34mVocê: \033[m').strip().lower()

        if not voce:
            print('\033[31mCHAT: Digite alguma coisa para conversarmos.\033[m')
            continue

        categoria = pergunta_resposta(voce)

        print(f'\033[32mCHAT: {responder(categoria)}\033[m')

        sleep(1)

        if categoria == 'despedidas':
            break