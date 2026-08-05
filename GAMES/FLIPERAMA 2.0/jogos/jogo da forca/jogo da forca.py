#jogo da forca

from random import choice

palavras = ['estudar', 'ler', 'programar', 'amar', 'quando', 'estrela', 'rainha', 'tambor', 'uva', 'ilha',
            'ovo', 'produtivo', 'sonhar', 'duvidar', 'insistir', 'hoje', 'janta', 'lutar', 'zebra',
            'cachorro', 'bolo', 'novo', 'move']

letras_usuario = []
chances = 6

palavra = choice(palavras)

def linha(tam = 42):
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

def mostrar_letras_usadas():
    print('Letras Usadas:')
    for letra in letras_usuario:
        print(f'{letra.upper()} ',end='')

def verifica_vitoria():
    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario: 
            ganhou = False
    return ganhou

cabeçalho('JOGO DA FORCA')
while True:
    #criar a nossa lógica
    print('\nPalavra: ', end='')
    mostrar_palavra()
    print(f'Você tem {chances} chances')
    try:
        while True:
            tentativa = input('Escolha uma letra para adivinhar: ').lower()[0]
            if tentativa.isalpha():
                break
            else:
                print('Letra inválida.')
    except IndexError:
        print('Não há valor digitado.')
        continue
    if tentativa not in palavra and tentativa not in letras_usuario:
        chances -= 1
    mostrar_linha()
    if tentativa not in letras_usuario:
        letras_usuario.append(tentativa)
    else:
        print('Você já tentou essa letra.')
        continue
    mostrar_letras_usadas()

    ganhou = verifica_vitoria()
     
    if chances == 0 or ganhou:
        break

mostrar_linha()
if ganhou:
    print(f'Parabéns, você ganhou o jogo. A palavra era: {palavra}')
else:
    print(f'Você perdeu! A palavra era: {palavra}')
