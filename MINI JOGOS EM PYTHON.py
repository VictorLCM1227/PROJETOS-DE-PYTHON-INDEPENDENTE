#Fliperama do Victor
from random import randint
from time import sleep
print('='*40)
print(f'{" FLIPERAMA DO VICTOR ":^40}')
print('='*40)
#cadastro do jogador
jogador_nome = input('Como gostaria de ser chamado? ')
print('-'*40)
while True:
    #menu principal
    print('''MENU:
        
    [1] Corrida de Cavalos
    [2] Par ou Ímpar
    [3] Jokenpô
    [4] Adivinhe o Número
    [5] Blackjack 21
    [6] Quiz Matemático
    [7] RPG
    [8] Jogo de Dados
    [0] Sair''')
    print('-'*40)
    opcao_menu = int(input(f'Escolha o que fazer agora {jogador_nome}: '))
    while opcao_menu > 8 or opcao_menu < 0:
        opcao_menu = int(input('Opção inválida! Escolha o que fazer agora: '))
    #jogos

    #Corrida de Cavalos
    if opcao_menu == 1:
        print(f'{" CORRIDA DE CAVALOS ":=^40}')
        cavalo1 = 0
        cavalo2 = 0
        cavalo3 = 0
        print('''REGRAS:
        APOSTE EM UM CAVALO:
        "=" representa 10 metros
        [1] para CAVALO 1
        [2] para CAVALO 2
        [3] para CAVALO 3''')
        apostaplayer = int(input('Em qual cavalo você aposta? '))
        if apostaplayer < 1 or apostaplayer > 3:
            print('APOSTA INVÁLIDA! TENTE NOVAMENTE!')
        else:
            apostapc = randint(1, 3)
            for c in range(0, 10):
                print(f'ROUND {c+1}')
                cavalo1 += randint(1, 10)
                cavalo2 += randint(1, 10)
                cavalo3 += randint(1, 10)
                print('cavalo 1: ', '='*cavalo1)
                print('cavalo 2: ', '='*cavalo2)
                print('cavalo 3: ', '='*cavalo3)
                print('-=-'*20)
                sleep(1)
            if cavalo1 > cavalo2 and cavalo1 > cavalo3:
                print('O CAVALO 1 VENCEU A CORRIDA!')
                vencedor = 1
            elif cavalo2 > cavalo1 and cavalo2 > cavalo3:
                print('O CAVALO 2 VENCEU A CORRIDA!')
                vencedor = 2
            elif cavalo3 > cavalo1 and cavalo3 > cavalo2:
                print('O CAVALO 3 VENCEU A CORRIDA')
                vencedor = 3
            else:
                print('HOUVE EMPATE! CORRIDA ANULADA!')
                vencedor = 0
            if apostaplayer == apostapc:
                print('JOGADOR e COMPUTADOR fizeram a mesma aposta!')
            else:
                if apostaplayer == vencedor:
                    print('JOGADOR VENCEU A APOSTA!')
                elif apostapc == vencedor:
                    print('COMPUTADOR VENCEU A APOSTA!')
                else:
                    print('NINGUÉM venceu a aposta!')
            print(f'CAVALO 1 correu {cavalo1*10} metros.')
            print(f'CAVALO 2 correu {cavalo2*10} metros.')
            print(f'CAVALO 3 correu {cavalo3*10} metros.')
            print(f'Você apostou no cavalo {apostaplayer} e o computador no cavalo {apostapc}.')

    #Par ou Ímpar
    elif opcao_menu == 2:
        print(f'{" IMPAR OU PAR ":=^40}')
        jogadorwins = pcwins = 0
        opcao = input('ÍMPAR ou PAR? [P/I] ').upper().strip()[0]
        while opcao not in 'PI':
            opcao = input(' Opção INVÁLIDA! Tente novamente! ÍMPAR ou PAR? [P/I] ').upper().strip()[0]
        jogador_numero = int(input('Escolha um número: '))
        print('IMPAR')
        sleep(1)
        print('OU')
        sleep(1)
        print('PAR!!!')
        pc = randint(0, 10)
        soma = jogador_numero + pc
        if opcao == 'I':
            print('JOGADOR Escolheu IMPAR e COMPUTADOR escolheu PAR')
        else:
            print('JOGADOR escolheu PAR e COMPUTADOR escolheu IMPAR')
        print(F'JOGADOR escolheu: {jogador_numero}')
        print(f'O COMPUTADOR escolheu {pc}')
        print(f'A SOMA foi: {soma}')
        if soma %2 == 0:
            resultado = 'P'
        else:
            resultado = 'I'
        if opcao == resultado:
            print('JOGADOR VENCEU')
            jogadorwins += 1
        else:
            print('COMPUTADOR VENCEU')
            pcwins += 1
        print('-=-'*20)
        if jogadorwins > pcwins:
            print(f'JOGADOR É O CAMPEÃO COM {jogadorwins} VITÓRIAS!')
        elif jogadorwins < pcwins:
            print(f'COMPUTADOR É O CAMPEÃO COM {pcwins} VITÓRIAS!')
        else:
            print(f'EMPATE! COMPUTADOR com {pcwins} e JOGADOR com {jogadorwins} VITÓRIAS!')


    #Jokenpô
    elif opcao_menu == 3:
        itens = ['PEDRA', 'PAPEL', 'TESOURA']
        print(f'{" VAMOS JOGAR JOKENPÔ ":=^40}')
        print('''Suas opções:
        [0] para PEDRA
        [1] para PAPEL
        [2] para TESOURA
            ''')
        jogador_vitorias = computador_vitorias = 0
        jogador_jogada = int(input('Sua jogada? '))
        while jogador_jogada > 2 or jogador_jogada < 0:
            print('Jogada inválida. Tente novamente!')
            jogador_jogada = int(input('Sua jogada? '))
        computador = randint(0,2)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print(f'Sua jogada: {itens[jogador_jogada]}')
        print(f'Jogada do computador: {itens[computador]}')
        if jogador_jogada == computador:
            print('EMPATE')
        elif (jogador_jogada == 0 and computador == 2) or (jogador_jogada == 1 and computador == 0) or (jogador_jogada == 2 and computador == 1):
                print('JOGADOR GANHOU!')
                jogador_vitorias += 1
        else:
            print('COMPUTADOR GANHOU!')
            computador_vitorias += 1
        print('=-=' * 20)
        if jogador_vitorias > computador_vitorias:
            print(f'Você venceu com {jogador_vitorias} vitórias enquanto o computador conseguiu apenas {computador_vitorias} vitórias.')
        elif jogador_vitorias < computador_vitorias:
                print(f'Você perdeu conseguindo apenas {jogador_vitorias} vitórias enquanto o computador conseguiu {computador_vitorias} vitórias.')
        else:
            print(f'Foi um empate! Ambos com {jogador_vitorias} vitórias.')

    #Adivinhe o Número
    elif opcao_menu == 4:
        print(f'{" ADIVINHE O NÚMERO ":=^40}')
        tentativas = 1
        computador = randint(0, 10)
        while True:
            print(f'Round: {tentativas}')
            jogador_palpite = int(input('Seu palpite: '))
            while jogador_palpite > 10 or jogador_palpite < 0:
                jogador_palpite = int(input('Palpite inválido. Tente novamente! Seu palpite: '))
            if jogador_palpite == computador:
                print('Parabéns! Você acertou!')
                print(f'E precisou de {tentativas} tentativas.')
                break
            elif jogador_palpite < computador:
                print('MAIS...')
            elif jogador_palpite > computador:
                print('MENOS...')
            tentativas += 1
            print('-'*40)
            

    #Blackjack 21
    elif opcao_menu == 5:
        jogador_pontos = randint(1, 10)
        print(f'Seus pontos: {jogador_pontos}')
        computador = randint(1, 10)
        while True:
            if jogador_pontos == 21:
                print('Você fez 21 pontos e venceu!')
                break
            if computador == 21:
                print('O computador fez 21 pontos e venceu!')
                break
            if jogador_pontos > 21:
                print(f'Você perdeu com {jogador_pontos} pontos.')
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
                computador += randint(1,10)
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

    #Quiz Matemático
    elif opcao_menu == 6:
        print(f'{" QUIZ ":=^80}')
        print('''REGRAS:
        -O jogador responderá 5 perguntas.
        -Cada resposta correta vale 1 ponto.
        -A pontuação será mostrada no final.''')
        acertos = 0

        pergunta1 = int(input('Quanto é 12 × 8? '))
        resposta1 = 96
        if pergunta1 == resposta1:
            print('Você acertou a primeira pergunta!')
            acertos +=1
        else:
            print('Você errou!')

        pergunta2 = int(input('Qual é a raiz quadrada de 144? '))
        resposta2 = 12

        if pergunta2 == resposta2:
            print('Você acertou a segunda pergunta!')
            acertos +=1
        else:
            print('Você errou!')

        pergunta3 = int(input('Quanto é 15²? '))
        resposta3 = 225
        if pergunta3 == resposta3:
            print('Você acertou a terceira pergunta!')
            acertos += 1
        else:
            print('Você errou!')

        pergunta4 = int(input('Quanto é 18 × 7? '))
        resposta4 = 126
        if pergunta4 == resposta4:
            print('Você acertou a quarta pergunta!')
            acertos += 1
        else:
            print('Você errou!')

        pergunta5 = int(input('Quanto é 1000 ÷ 25? '))
        resposta5 = 40
        if pergunta5 == resposta5:
            print('Você acertou a quinta pergunta!')
            acertos += 1
        else:
            print('Você errou!')

        totacertos = acertos * 20
        print(f'O seu desempenho foi de {totacertos}%')
        print(f'Você acertou {acertos} perguntas.')
        print(f'Você errou {5 - acertos} perguntas.')
        print(f'A sua pontuação total foi de {acertos} pontos.')

    #RPG
    elif opcao_menu == 7:
        print(f'{" RPG SIMPLES ":=^40}')
        vitorias = 0
        derrotas = 0
        vidahero = 50
        for c in range(0, 10):
            print(f'BATALHA {c+1}')
            dano = randint(-10, 20)
            if vidahero < 1:
                print('DERROTADO!')
            else:
                print(f'Vida do jogador: {vidahero}')
            print(f'Efeito da batalha na vida do jogador: +({dano*-1})')
            vidahero = vidahero - dano
            if vidahero < 1:
                print('DERROTADO!')
                derrotas = 1
                break
            else:
                print(f'vida restante: {vidahero}')
            print('-=-'*40)
            sleep(1)
            if vidahero >= 1:
                vitorias = vitorias + 1
        print(f'Vida restante: {vidahero}')
        print(f'VITÓRIAS: {vitorias}')
        print(f'Derrotas: {derrotas}')

    #Jogo de Dados
    elif opcao_menu == 8:
        lados = int(input('Quantos lados gostaria no dado? O minimo é um dado de 6 lados.  '))
        if lados < 6:
            lados = 6
        print(f'Você escolheu um dado de {lados} lados.')
        dado = randint(1, lados)
        print('O dado foi jogado...')
        sleep(1)
        print(f'O dado caiu no lado {dado}.')

    #Sair
    elif opcao_menu == 0:
        print('SAINDO...')
        break
