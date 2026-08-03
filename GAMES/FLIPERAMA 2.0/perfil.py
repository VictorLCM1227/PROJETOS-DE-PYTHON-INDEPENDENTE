#perfil
from utilidades import leiaInt, linha, cabeçalho, menu

def mostrar_perfil(ficha_do_jogador):
    cabeçalho('PERFIL')
    #desempacotar e mostrar dicionario
    for atributo, valor in ficha_do_jogador.items():
        print(f'{atributo}: {valor}')
    print(linha())
    taxa_de_vitoria = ficha_do_jogador['vitoria'] / ficha_do_jogador['partidas']
    print(f'Taxa de vitória: {taxa_de_vitoria:.2f}%')