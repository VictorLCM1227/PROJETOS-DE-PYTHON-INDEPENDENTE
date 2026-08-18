acertos = 0
erros = 0
total_perguntas = 0


def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não informar um número.')
            return 0
        else:
            return numero


def menu():
    print('=' * 30)
    print('MENU')
    print('[0] SAIR')
    print('[1] JOGAR')
    print('=' * 30)


def menu_dificuldade():
    print('=' * 30)
    print('ESCOLHA A DIFICULDADE')
    print('[1] FÁCIL')
    print('[2] MÉDIO')
    print('[3] DIFÍCIL')
    print('=' * 30)


def escolhe_dificuldade(dificuldade):
    if dificuldade == 1:
        return 'fácil'
    elif dificuldade == 2:
        return 'médio'
    elif dificuldade == 3:
        return 'difícil'


def soma_acertos():
    global acertos

    acertos += 1
    print('PARABÉNS! Você acertou a pergunta!')


def soma_erros():
    global erros

    erros += 1
    print('Você errou a pergunta.')


def jogar(dificuldade):
    global total_perguntas

    print('\nVamos jogar!')
    print('-' * 30)

    for pergunta_resposta in perguntas[dificuldade]:

        pergunta = pergunta_resposta[0]
        resposta_correta = pergunta_resposta[1]

        resposta_jogador = leiaInt(f'Responda: {pergunta} ')

        if resposta_jogador == resposta_correta:
            soma_acertos()
        else:
            soma_erros()
            print(f'A resposta correta era {resposta_correta}.')

        total_perguntas += 1
        print('-' * 30)


def resultado():
    print('=' * 30)
    print('RESULTADO DA PARTIDA')
    print(f'Acertos: {acertos}')
    print(f'Erros: {erros}')
    print(f'Total de perguntas: {total_perguntas}')

    if total_perguntas > 0:
        aproveitamento = acertos / total_perguntas * 100
        print(f'Aproveitamento: {aproveitamento:.2f}%')

    print('=' * 30)


perguntas = {

    'fácil': [

        # Soma
        ('2 + 3', 5),
        ('8 + 7', 15),
        ('9 + 6', 15),
        ('14 + 5', 19),

        # Subtração
        ('10 - 4', 6),
        ('20 - 13', 7),
        ('18 - 9', 9),
        ('25 - 17', 8),

        # Múltiplos
        ('O número 24 é múltiplo de qual número? (8)', 8),
        ('O número 30 é múltiplo de qual número? (6)', 6),

        # Divisores
        ('Quantos divisores possui o número 6?', 4),
        ('Quantos divisores possui o número 10?', 4),

        # Mediana
        ('Mediana de 2, 4, 6?', 4),
        ('Mediana de 3, 5, 9?', 5),
        ('Mediana de 8, 10, 12?', 10)
    ],

    'médio': [

        # Multiplicação
        ('6 × 7', 42),
        ('8 × 9', 72),
        ('12 × 11', 132),
        ('15 × 8', 120),

        # Divisão
        ('54 ÷ 6', 9),
        ('81 ÷ 9', 9),
        ('96 ÷ 8', 12),
        ('144 ÷ 12', 12),

        # Múltiplos
        ('Qual é o menor múltiplo de 9 maior que 50?', 54),
        ('Qual é o menor múltiplo de 7 maior que 40?', 42),

        # Divisores
        ('Quantos divisores possui o número 12?', 6),
        ('Quantos divisores possui o número 18?', 6),

        # Mediana
        ('Mediana de 5, 8, 12?', 8),
        ('Mediana de 10, 14, 18?', 14),
        ('Mediana de 9, 15, 20?', 15)
    ],

    'difícil': [

        # Expressões
        ('(8 + 4) × 3', 36),
        ('(15 - 7) × (6 + 2)', 64),
        ('(18 ÷ 3) × (5 + 1)', 36),

        # Potência
        ('2³', 8),
        ('5² + 4²', 41),
        ('3⁴', 81),
        ('6²', 36),

        # Raiz quadrada
        ('√144', 12),
        ('√225', 15),
        ('√196', 14),

        # Múltiplos
        ('Qual é o menor múltiplo de 13 maior que 100?', 104),
        ('Qual é o menor múltiplo de 17 maior que 150?', 153),

        # Divisores
        ('Quantos divisores possui o número 24?', 8),
        ('Quantos divisores possui o número 36?', 9),

        # Mediana
        ('Mediana de 15, 28, 33?', 28),
        ('Mediana de 42, 37, 50?', 42)
    ]
}


while True:

    menu()

    while True:
        escolha = leiaInt('>>> Escolha: ')

        if escolha in (0, 1):
            break

        print('Opção inválida.')

    if escolha == 0:
        print('Saindo...')
        break

    menu_dificuldade()

    while True:
        dificuldade = leiaInt(
            '>>> Qual dificuldade gostaria de jogar? '
        )

        if dificuldade in (1, 2, 3):
            break

        print('Opção inválida.')

    dificuldade_escolhida = escolhe_dificuldade(dificuldade)

    print('-' * 30)

    jogar(dificuldade_escolhida)

    resultado()

    acertos = 0
    erros = 0
    total_perguntas = 0