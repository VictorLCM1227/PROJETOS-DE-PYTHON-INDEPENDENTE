

def menu():
    print('''MENU:
[0] SAIR
[1] JOGAR''')
    

def jogar(dificuldade):
    global total_perguntas
    print('Vamos jogar!')
    for pergunta_resposta in perguntas[dificuldade]:
        resposta_jogador = leiaInt(f'Responda: {pergunta_resposta[0]} ')
        if resposta_jogador == pergunta_resposta[1]:
            soma_acertos()
        else:
            soma_erros()
        total_perguntas += 1

def resultado():
    aproveitamento = acertos / total_perguntas * 100
    print('=' * 30)
    print('Resultado da partida')
    print(f'Acertos: {acertos}')
    print(f'Erros: {erros}')
    print(f'Total de perguntas: {total_perguntas}')
    print(f'Aproveitamento {aproveitamento:.2f}%')
    print('=' * 30)


def soma_acertos():
    print('PARABÉNS! Você acertou a pergunta!')
    global acertos
    acertos += 1


def soma_erros():
    print('Você errou a pergunta.')
    global erros
    erros += 1


def menu_dificuldade():
    print('''Escolha a dificuldade:
[1] FÁCIL (soma e subtração)
[2] MÉDIO (multiplicação e divisão)
[3] DIFÍCIL (expressões, potência e raiz quadrada)''')


def escolhe_dificuldade(dificuldade):
    if dificuldade == 1:
        dificuldade_escolhida = 'fácil'
    elif dificuldade == 2:
        dificuldade_escolhida = 'médio'
    elif dificuldade == 3:
        dificuldade_escolhida = 'difícil'
    return dificuldade_escolhida

def leiaInt(n):
    while True:
        teste = input(n)
        if teste.isdigit():
            teste = int(teste)
            return teste
        else:
            print('ERRO! Digite um número válido.')


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
        escolha = int(input('>>>Escolha: '))
        if escolha == 0 or escolha == 1:
            break
        print('Opção inválida.')

    if escolha == 0:
        print('Saindo...')
        break

    elif escolha == 1:
        menu_dificuldade()
        while True:
            dificuldade = int(input('>>> Qual dificuldade gostaria de jogar? '))
            if 0 < dificuldade <= 3:
                break
            print('Opção inválida.')
        print('-' * 30)
        dificuldade_escolhida = escolhe_dificuldade(dificuldade)
        jogar(dificuldade_escolhida)
        resultado()
        acertos = erros = total_perguntas = 0