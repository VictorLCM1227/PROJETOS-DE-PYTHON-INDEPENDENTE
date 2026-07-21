#Fliperama do Victor
from random import randint
from time import sleep

print('='*40)
print(f'{" MINI JOGOS DO VICTOR ":^40}')
print('='*40)
jogador_nome = input('Como gostaria de ser chamado? ')
print('-'*40)
extrato = []
saldo = 0
#funções

def menu_principal():
    print('''MENU:
        
    [1] Corrida de Cavalos
    [2] Par ou Ímpar
    [3] Jokenpô
    [4] Adivinhe o Número
    [5] Blackjack 21
    [6] Quiz Matemático
    [7] RPG
    [8] Jogo de Dados
    [9]Carteira
    [0] Sair''')
    print('-'*40)

def corrida_de_cavalos():
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

    while True:
        aposta_jogador = int(input(f'Em qual cavalo você aposta? {jogador_nome}: '))
        if 1 <= aposta_jogador <= 3:
            break
        print('Opção inválida! Escolha um cavalo de 1 a 3: ')
    aposta_computador = randint(1, 3)

    for c in range(0, 10):
        print(f'ROUND {c+1}')
        cavalo1 += randint(1, 10)
        cavalo2 += randint(1, 10)
        cavalo3 += randint(1, 10)
        print('🐎 cavalo 1: ', '=' * cavalo1)
        print('🐎 cavalo 2: ', '=' * cavalo2)
        print('🐎 cavalo 3: ', '=' * cavalo3)
        print('-=-' * 20)
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

    if aposta_jogador == aposta_computador:
        print('JOGADOR e COMPUTADOR fizeram a mesma aposta!')
    else:
        if aposta_jogador == vencedor:
            print('JOGADOR VENCEU A APOSTA!')
#aposta
        elif aposta_computador == vencedor:
            print('COMPUTADOR VENCEU A APOSTA!')
        else:
            print('NINGUÉM venceu a aposta!')

    print(f'CAVALO 1 correu {cavalo1 * 10} metros.')
    print(f'CAVALO 2 correu {cavalo2 * 10} metros.')
    print(f'CAVALO 3 correu {cavalo3 * 10} metros.')
    print(f'Você apostou no cavalo {aposta_jogador} e o computador no cavalo {aposta_computador}.')

def par_ou_impar():
    print(f'{" IMPAR OU PAR ":=^40}')
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
    else:
        print('COMPUTADOR VENCEU')
    print('-=-'*20)

def jokenpo():
    itens = ['PEDRA', 'PAPEL', 'TESOURA']
    print(f'{" VAMOS JOGAR JOKENPÔ ":=^40}')
    print('''Suas opções:
    [0] para PEDRA
    [1] para PAPEL
    [2] para TESOURA
        ''')
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
    else:
        print('COMPUTADOR GANHOU!')
    print('=-=' * 20)

def adivinhe_o_numero():
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

def quiz_matemático():
    print(f'{" QUIZ ":=^80}')
    print('''REGRAS:
    -O jogador responderá 5 perguntas.
    -Cada resposta correta vale 1 ponto.
    -A pontuação será mostrada no final.''')

    perguntas = [
        ('Quanto é 12 × 8? ', 96),
        ('Qual é a raiz quadrada de 144? ', 12),
        ('Quanto é 15²? ', 225),
        ('Quanto é 18 × 7? ', 126),
        ('Quanto é 1000 ÷ 25? ', 40)
    ]

    acertos = 0

    for pergunta, resposta in perguntas:
        if int(input(pergunta + ' ')) == resposta:
            acertos += 1
            print('Você acertou a pergunta!')
        else: 
            print('Você errou a pergunta!')

    totacertos = acertos * 20
    print(f'O seu desempenho foi de {totacertos}%')
    print(f'Você acertou {acertos} perguntas.')
    print(f'Você errou {5 - acertos} perguntas.')
    print(f'A sua pontuação total foi de {acertos} pontos.')

def rpg():
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
        if dano >= 0:
            print(f'Você perdeu {dano} de vida.')
        else:
            print(f'Você recuperou {-dano} de vida.')
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

def jogo_de_dados():
    lados = int(input('Quantos lados gostaria no dado? O minimo é um dado de 6 lados.  '))
    if lados < 6:
        lados = 6
    print(f'Você escolheu um dado de {lados} lados.')
    dado = randint(1, lados)
    print('O dado foi jogado...')
    sleep(1)
    print(f'O dado caiu no lado {dado}.')

def carteira():
    global saldo
    global extrato
    print(f'{" CARTEIRA ":^30}')
    print('=' * 30)
    while True:
        print('''[0] Para sair
[1] Consultar saldo
[2] Depositar dinheiro
[3] Sacar dinheiro
[4] Mostrar o extrato''')
        print('-' * 30)
        while True:
            opcao = int(input('>>> O que deseja fazer? '))
            if opcao in (0, 1, 2, 3, 4):
                break
            print('Opção inváliida. Somente 0, 1, 2, 3 ou 4.')
        if opcao == 0:
            print('Saindo...')
            break

        elif opcao == 1:
            print('Consultando Saldo...')
            sleep(0.5)
            print(f'Seu Saldo é de R${saldo}')

        elif opcao == 2:
            deposito = int(input('Valor do depósito: R$'))
            if deposito < 1:
                print('O valor do depósito deve ser maior que zero.')
            else:
                print('Depositando...')
                sleep(0.5)
                saldo += deposito
                extrato.append(deposito)

        elif opcao == 3:
            saque = int(input('Valor do Saque: R$'))
            if saque < 1:
                print('O valor do saque deve ser maior que zero.')
            else:
                if saque > saldo:
                    print('Saldo Insuficiente.')
                else:
                    print('Sacando...')
                    sleep(0.5)
                    extrato.append(saque * (-1))
                    saldo -= saque
                    print(f'Saque de R${saque} realizado com sucesso!')

        elif opcao == 4:
            print('Abrindo extrato:')
            sleep(0.5)
            if not extrato:
                print('Ainda não houve Transações.')
            else:
                for transação in extrato:
                    if transação > 0:
                        print(f'Depósito de R${abs(transação)}')
                    else:
                        print(f'Saque de R${abs(transação)}')
        print('-' * 30)
    print('=' * 30)
        
while True:
    menu_principal()
    while True:
        opcao_menu = int(input(f'Escolha o que fazer agora {jogador_nome}: '))
        if 0 <= opcao_menu <= 9:
            break
        print('Opção inválida! Escolha o que fazer agora: ')

#jogos

#Sair
    if opcao_menu == 0:
        print('SAINDO...')
        break

#Corrida de Cavalos
    if opcao_menu == 1:
        corrida_de_cavalos()

#Par ou Ímpar
    elif opcao_menu == 2:
        par_ou_impar()
        

#Jokenpô
    elif opcao_menu == 3:
        jokenpo()

#Adivinhe o Número
    elif opcao_menu == 4:
        adivinhe_o_numero()
            

#Blackjack 21
    elif opcao_menu == 5:
        blackjack_21()
        

#Quiz Matemático
    elif opcao_menu == 6:
        quiz_matemático()


#RPG
    elif opcao_menu == 7:
        rpg()
        
#Jogo de Dados
    elif opcao_menu == 8:
        jogo_de_dados()

#Carteira
    elif opcao_menu == 9:
        carteira()


#Falta: adiconar o sistema de apostas para ganhar dinheiro, colocar a loja de compra de itens pra nickname tipo emoji e cor da fonte e fundo seguindo o padrão ANSI