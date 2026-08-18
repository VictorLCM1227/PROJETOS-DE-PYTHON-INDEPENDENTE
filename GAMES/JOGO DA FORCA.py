from random import choice

palavras = [
    'estudar', 'ler', 'programar', 'amar', 'quando',
    'estrela', 'rainha', 'tambor', 'uva', 'ilha',
    'ovo', 'produtivo', 'sonhar', 'duvidar',
    'insistir', 'hoje', 'janta', 'lutar', 'zebra',
    'cachorro', 'bolo', 'novo', 'move'
]

letras_usuario = []
chances = 6
palavra = choice(palavras)


def linha(tam=42):
    return '-' * tam


def mostrar_linha():
    print(f'\n{linha()}')


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def mostrar_palavra():
    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()


def mostrar_letras_usadas():
    print('Letras usadas: ', end='')

    for letra in letras_usuario:
        print(letra.upper(), end=' ')

    print()


def verificar_vitoria():
    for letra in palavra:
        if letra not in letras_usuario:
            return False

    return True


def escolher_letra():
    while True:
        tentativa = input('Escolha uma letra para adivinhar: ').strip().lower()

        if not tentativa:
            print('Você não digitou nenhuma letra.')
            continue

        if len(tentativa) > 1:
            print('Digite apenas uma letra.')
            continue

        if not tentativa.isalpha():
            print('Digite uma letra válida.')
            continue

        return tentativa


def jogar():
    global chances

    while True:

        print('\nPalavra: ', end='')
        mostrar_palavra()

        print(f'Chances restantes: {chances}')
        mostrar_letras_usadas()

        tentativa = escolher_letra()

        if tentativa in letras_usuario:
            print('Você já tentou essa letra.')
            continue

        letras_usuario.append(tentativa)

        if tentativa in palavra:
            print('Acertou!')
        else:
            chances -= 1
            print('Errou!')

        if verificar_vitoria():
            return True

        if chances == 0:
            return False

        mostrar_linha()


cabeçalho('JOGO DA FORCA')

ganhou = jogar()

mostrar_linha()

if ganhou:
    print(f'Parabéns! Você ganhou!')
    print(f'A palavra era: {palavra}')
else:
    print('Você perdeu!')
    print(f'A palavra era: {palavra}')