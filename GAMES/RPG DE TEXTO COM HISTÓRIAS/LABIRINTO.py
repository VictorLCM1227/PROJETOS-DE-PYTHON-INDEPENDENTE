
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
        try:
            movimento = input('>>>Digite um movimneto: ').strip().upper()[0]
        except IndexError:
            print('ERRO! Movimento não informado.')
        else:
            if movimento in 'WASD':
                break
            print('Opção inválida.')
    print(f'Você apertou {movimento}')
    return movimento




def movimenta_jogador():
    while True:
        global coluna_do_jogador, linha_do_jogador
        movimento = valida_movimento()
        proxima_posicao_linha = linha_do_jogador
        proxima_posicao_coluna = coluna_do_jogador

        if movimento == 'W':
            proxima_posicao_linha -= 1
            if '#' in labirinto[proxima_posicao_linha][proxima_posicao_coluna]:
                print('Há uma parede no caminho. Tente novamente.')
            else:
                linha_do_jogador -= 1   
                break

        elif movimento == 'A':
            proxima_posicao_coluna -= 1
            if '#' in labirinto[proxima_posicao_linha][proxima_posicao_coluna]:
                print('Há uma parede no caminho. Tente novamente.')
            else:
                coluna_do_jogador -= 1
                break

        elif movimento == 'S':
            proxima_posicao_linha += 1
            if '#' in labirinto[proxima_posicao_linha][proxima_posicao_coluna]:
                print('Há uma parede no caminho. Tente novamente.')
            else:
                linha_do_jogador += 1
                break

        elif movimento == 'D':
            proxima_posicao_coluna += 1
            if '#' in labirinto[proxima_posicao_linha][proxima_posicao_coluna]:
                print('Há uma parede no caminho. Tente novamente.')
            else:
                coluna_do_jogador += 1
                break

def verifica_vitoria():
    if 'S' in labirinto[linha_do_jogador][coluna_do_jogador]:
        return True

def linha(tam = 42):
    return '-' * tam 

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

cabecalho('ESCAPE DO LABIRINTO')

while True:
    mostrar_labirito()
    print(linha())
    movimenta_jogador()
    if verifica_vitoria():
        break
print('Parabéns! você escapou do labirinto!')
