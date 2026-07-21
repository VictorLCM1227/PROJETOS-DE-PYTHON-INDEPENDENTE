from random import randint

def menu():
    print('''MENU:
[0] SAIR
[1] JOGAR''')
    

def jogar(dificuldade):
    print('Vamos jogar!')
    pergunta_resposta_aleatoria = randint(0, len(perguntas[dificuldade]) - 1)
    pergunta_atual = perguntas[dificuldade][pergunta_resposta_aleatoria][0]
    resposta_atual = perguntas[dificuldade][pergunta_resposta_aleatoria][1]
    resposta_jogador = float(input(f'Responda: {pergunta_atual} '))
    if resposta_jogador == resposta_atual:
        soma_acertos()
    else:
        print('Você errou a pergunta.')
    



def resultado():
    print('=' * 30)
    print('Resultado da partida')
    print(f'Acertos: {acertos}')
    print(f'Pontos: {pontos}')
    print('=' * 30)


def soma_acertos():
    print('PARABÉNS! Você acertou a pergunta!')
    global pontos, acertos
    pontos += 1
    acertos += 1

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


pontos = acertos = erros = 0

perguntas = {
    'fácil': [
        ('2 + 3', 5),
        ('10 - 4', 6),
        ('8 + 7', 15),
        ('20 - 13', 7),
        ('9 + 6', 15)
    ],

    'médio': [
        ('6 × 7', 42),
        ('54 ÷ 6', 9),
        ('8 × 9', 72),
        ('81 ÷ 9', 9),
        ('12 × 11', 132)
    ],

    'difícil': [
        ('(8 + 4) × 3', 36),
        ('2³', 8),
        ('√144', 12),
        ('(15 - 7) × (6 + 2)', 64),
        ('5² + 4²', 41)
    ]
}

menu()
while True:
    escolha = int(input('>>>Escolha: '))
    if escolha == 0 or escolha == 1:
        break
    print('Opção inválida.')

if escolha == 0:
    print('Saindo...')

elif escolha == 1:
    menu_dificuldade()
    while True:
        dificuldade = int(input('>>> Qual dificuldade gostaria de jogar? '))
        if 0 < dificuldade <= 3:
            break
        print('Opção inválida.')
    jogar(escolhe_dificuldade(dificuldade))
    resultado()
