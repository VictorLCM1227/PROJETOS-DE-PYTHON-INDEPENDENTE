# jogo_da_forca.py

from random import choice

from utilidades import linha, cabeçalho


PALAVRAS = [
    'estudar',
    'ler',
    'programar',
    'amar',
    'quando',
    'estrela',
    'rainha',
    'tambor',
    'uva',
    'ilha',
    'ovo',
    'produtivo',
    'sonhar',
    'duvidar',
    'insistir',
    'hoje',
    'janta',
    'lutar',
    'zebra',
    'cachorro',
    'bolo',
    'novo',
    'move'
]


def jogo_da_forca():

    palavra = choice(PALAVRAS)

    letras_usuario = []
    chances = 6

    def mostrar_palavra():

        for letra in palavra:

            if letra in letras_usuario:
                print(letra, end=' ')

            else:
                print('_', end=' ')

    def mostrar_letras_usadas():

        print('Letras usadas:', end=' ')

        for letra in letras_usuario:
            print(letra.upper(), end=' ')

        print()

    def verifica_vitoria():

        for letra in palavra:

            if letra not in letras_usuario:
                return False

        return True

    cabeçalho('JOGO DA FORCA')

    while chances > 0:

        print('\nPalavra: ', end='')
        mostrar_palavra()

        print(f'\nVocê tem {chances} chances.')

        mostrar_letras_usadas()

        while True:

            tentativa = input(
                'Escolha uma letra para adivinhar: '
            ).strip().lower()

            if len(tentativa) != 1:
                print('Digite apenas uma letra.')
                continue

            if not tentativa.isalpha():
                print('Letra inválida.')
                continue

            break

        if tentativa in letras_usuario:

            print('Você já tentou essa letra.')
            continue

        letras_usuario.append(tentativa)

        if tentativa not in palavra:
            chances -= 1

        print(linha())

        if verifica_vitoria():
            print(
                f'Parabéns, você ganhou o jogo! '
                f'A palavra era: {palavra}'
            )

            return 'vitoria'

    print(
        f'Você perdeu! '
        f'A palavra era: {palavra}'
    )

    return 'derrota'