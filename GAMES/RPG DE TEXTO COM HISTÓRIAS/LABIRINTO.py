
labirinto = [
             ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',],
             ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ],
             ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ',  '#',],
             ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#',],
             ['#', '#', '#', ' ',  '#', '#', '#', '#', ' ', '#',],
             ["#", ' ', ' ', ' ', ' ', ' ', ' ', '#', 'S', '#',],
             ['#', '#', '#','#', '#', '#', '#', '#', '#', '#']
            ]

linha_do_jogador = 2
coluna_do_jogador = 2

def mostrar_labirito():
    for linha in range(7):
        for coluna in range(10):
            if linha == linha_do_jogador and coluna == coluna_do_jogador:
                print('P', end='')
            else:
                print(labirinto[linha][coluna], end='')
        print()

def movimentos():
    print('''[W] CIMA
[A] ESQUERDA
[S] BAIXO
[D] DIREITA''')

def valida_movimento():
    while True:
        movimentos()
        movimento = input('Digite um movimneto: ').strip().upper()[0]
        if movimento in 'WASD':
            break
        print('Opção inválida.')
    print(f'Você apertou {movimento}')
    return movimento

def movimenta_jogador():
    global coluna_do_jogador, linha_do_jogador
    movimento = valida_movimento()
    if movimento == 'W':
        linha_do_jogador -= 1
    elif movimento == 'A':
        coluna_do_jogador -= 1
    elif movimento == 'S':
        linha_do_jogador += 1
    elif movimento == 'D':
        coluna_do_jogador += 1

mostrar_labirito()
movimenta_jogador()
mostrar_labirito()
