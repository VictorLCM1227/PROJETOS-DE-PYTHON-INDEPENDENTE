print('LABIRINTO: ')
print('-' * 30)
print('''P é o jogador.
S é a saída.
# são paredes.
Espaços são caminhos livres.''')
print('-' * 30)
print('''
########
#P     #
# ###  #
#     S#
########
      ''')
direcao = input('''Faça um movimento:
[W] CIMA
[A] ESQUERDA
[D] DIREITA
[S] BAIXO''').strip().upper()[0]