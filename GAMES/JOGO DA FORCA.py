
palavra = 'python'

letras_usuario = []

chances = 6

ganhou = False

while True:
    #criar a nossa lógica
    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f'Você tem {chances} chances')
    tentativa = input('Escolha uma letra para adivinhar: ').lower()[0]
    if tentativa not in letras_usuario:
        letras_usuario.append(tentativa)
    else:
        print('Você já tentou essa letra.')
    if tentativa not in palavra:
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario: 
            ganhou = False 

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, você ganhou o jogo. A palavra era: {palavra}')
else:
    print(f'Você perdeu! A palavra era: {palavra}')
