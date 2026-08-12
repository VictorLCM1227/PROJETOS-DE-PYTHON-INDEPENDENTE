#conquistas
def controla_conquistas(ficha_do_jogador):
    if ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] > 0:
        if not ficha_do_jogador['conquistas']['primeira_vitoria']:
            ficha_do_jogador['conquistas']['primeira_vitoria'] = True
            print('🏆 Conquista desbloqueada: 1° vitória!')

    
    if ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] >= 10:
        if not ficha_do_jogador['conquistas']['10_vitorias']:
            ficha_do_jogador['conquistas']['10_vitorias'] = True
            print('🏆 Conquista desbloqueada: 10 vitórias!')


    if ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] >= 50:
            if not ficha_do_jogador['conquistas']['50_vitorias']:
                ficha_do_jogador['conquistas']['50_vitorias'] = True
                print('🏆 Conquista desbloqueada: 50 vitórias!')


    if ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] >= 100:
            if not ficha_do_jogador['conquistas']['100_vitorias']:
                ficha_do_jogador['conquistas']['100_vitorias'] = True
                print('🏆 Conquista desbloqueada: 100 vitórias!')


    if ficha_do_jogador['carteira']['saldo'] >= 1000000:
            if not ficha_do_jogador['conquistas']['milionario']:
                ficha_do_jogador['conquistas']['milionario'] = True
                print('🏆 Conquista desbloqueada: milionário!')