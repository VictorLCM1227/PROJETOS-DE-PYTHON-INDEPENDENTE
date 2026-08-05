#blackjack

def blackjack_21():
    jogador_pontos = randint(1, 10)
    print(f'Seus pontos: {jogador_pontos}')
    computador = randint(1, 10)
    while computador < 17:
        computador += randint(1,10)
    while True:
        if jogador_pontos == 21:
            print('Você fez 21 pontos e venceu!')
            print(f'Enquanto o computador fez {computador} pontos')
            break
        if computador == 21:
            print('O computador fez 21 pontos e venceu!')
            break
        if jogador_pontos > 21:
            print(f'Você perdeu com {jogador_pontos} pontos.')
            print(f'Enquanto o computador fez {computador} pontos')
            break
        if computador > 21:
            print(f'Você venceu porque o computador passou de 21 com {computador} pontos.')
            break
        escolha = input('Comprar ou parar? [C/P]').strip().upper()[0]
        while escolha not in 'CP':
            escolha = input('Opção inválida. Tente novamente! Comprar ou parar? [C/P]').strip().upper()[0]
        if escolha == 'C':
            jogador_pontos += randint(1,10)
            print(f'Seus pontos: {jogador_pontos}')
        else:
            if jogador_pontos > computador:
                print(f'Você venceu com o total de {jogador_pontos} enquanto o computador conseguiu apenas {computador} pontos')
                break
            elif jogador_pontos < computador:
                print(f'Você perdeu porque o computador chegou mais próximo de 21 com {computador} enquanto você conseguiu apenas {jogador_pontos} pontos.')
                break
            else:
                print(f'EMPATE! Ambos com {jogador_pontos} pontos.')
                break