#jogador

def criar_estatisticas_jogo():
    return {
        'partidas': 0,
        'vitorias': 0,
        'derrotas': 0,
        'empates': 0,
        'sequencia_atual': 0,
        'melhor_sequencia': 0,
        'dinheiro_ganho': 0,
        'dinheiro_perdido': 0,
        'maior_aposta': 0
    }

ficha_do_jogador = {
    'nome': input('Qual o seu nome? ').strip(),
    'extrato': [],
    
    'estatisticas_gerais': {
        'partidas_totais':  0,
        'vitorias_totais': 0,
        'derrotas_totais': 0,
        'empates_totais': 0,
        'dinheiro_ganho_total': 0,
        'dinheiro_perdido_total':0,
        },
    
    
    
    
    'conquistas': {
        'primeira_vitoria': False,
        '10_vitorias': False,
        '50_vitorias': False,
        '100_vitorias': False,
        'milionario': False
    },
    'carteira': {
        
        'saldo': 10,
        'maior_aposta_feita' :0,
        
    },

    'inventario': {
    'cores_de_fundo': [],
    'cores_de_fonte': [],
    'emojis': []
    },

    'equipado': {
    'cor_de_fundo': None,
    'cor_de_fonte': None,
    'emoji': None
    },
    

    'estatisticas_jogos': {
    'jokenpo': criar_estatisticas_jogo(),
    'par_ou_impar': criar_estatisticas_jogo(),
    'adivinhe_o_numero': criar_estatisticas_jogo(),
    'blackjack': criar_estatisticas_jogo(),
    'corrida_de_cavalos': criar_estatisticas_jogo(),
    'dados': criar_estatisticas_jogo(),
    'jogo-da-forca': criar_estatisticas_jogo(),
    'jogo-da-velha': criar_estatisticas_jogo()
}
}
