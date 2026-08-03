#perfil
from utilidades import leiaInt, linha, cabeçalho, menu

def mostrar_perfil(ficha_do_jogador):
    cabeçalho('PERFIL')
    #desempacotar e mostrar dicionario
    for atributo, valor in ficha_do_jogador.items():
        print(f'{atributo}: {valor}')