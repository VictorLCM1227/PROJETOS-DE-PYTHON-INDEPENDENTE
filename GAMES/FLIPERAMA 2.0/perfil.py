#perfil
from utilidades import leiaInt, linha, cabeçalho, menu

def mostrar_perfil(ficha_do_jogador):
    print(f'Nome: {ficha_do_jogador["nome"]}')
    
    print('===== ESTATÍSTICAS GERAIS =====')
    for atributo, valor in ficha_do_jogador['estatisticas_gerais'].items():
            print(f"{atributo.replace('_', ' ').title()}: {valor}")
    if ficha_do_jogador['estatisticas_gerais']['partidas_totais'] > 0:
        taxa_de_vitoria = (ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] / ficha_do_jogador['estatisticas_gerais']['partidas_totais']) * 100
    else:
        taxa_de_vitoria = 0
    print(f'Taxa de vitória: {taxa_de_vitoria:.2f}%')
        
    print('===== CARTEIRA =====')
    for atributo, valor in ficha_do_jogador['carteira'].items():
        print(f"{atributo.replace('_', ' ').title()}: {valor}")

    
def ver_estatísticas_dos_jogos(ficha_do_jogador):
    for nome, jogo in ficha_do_jogador['estatisticas_jogos'].items():
        print(f"===== {nome.replace('_', ' ').title()} =====")
        for atributo, valor in jogo.items():
                print(f"{atributo.replace('_', ' ').title()}: {valor}")

