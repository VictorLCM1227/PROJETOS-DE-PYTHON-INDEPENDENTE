#dados

def jogo_de_dados():
    lados = int(input('Quantos lados gostaria no dado? O minimo é um dado de 6 lados.  '))
    if lados < 6:
        lados = 6
    print(f'Você escolheu um dado de {lados} lados.')
    dado = randint(1, lados)
    print('O dado foi jogado...')
    sleep(1)
    print(f'O dado caiu no lado {dado}.')