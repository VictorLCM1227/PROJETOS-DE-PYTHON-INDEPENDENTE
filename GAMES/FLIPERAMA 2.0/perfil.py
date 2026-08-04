#perfil
from utilidades import leiaInt, linha, cabeçalho, menu

def mostrar_perfil(ficha_do_jogador):
    cabeçalho('PERFIL')
    #desempacotar e mostrar dicionario
    for atributo, valor in ficha_do_jogador.items():
        print(f'{atributo}: {valor}')
    print(linha())
    if ficha_do_jogador['partidas_totais'] > 0:
        taxa_de_vitoria = ficha_do_jogador['vitoria_totais'] / ficha_do_jogador['partidas_totais']
        print(f'Taxa de vitória: {taxa_de_vitoria:.2f}%')

'''
5. Melhorar o perfil

Hoje você imprime o dicionário inteiro.

Isso funciona para depuração, mas um perfil pode ficar bem mais organizado, mostrando algo como:

Nome

Saldo

Partidas

Vitórias

Derrotas

Empates

Taxa de vitória

Dinheiro ganho

Dinheiro perdido

Maior aposta

Depois disso, imprimir as estatísticas de cada jogo separadamente.
'''