def controla_conquitas(ficha_do_jogador):
    if ficha_do_jogador['estatisticas_gerais']['partidas_totais'] > 0:
        ficha_do_jogador['conquistas']['primeira_vitoria'] = True
    