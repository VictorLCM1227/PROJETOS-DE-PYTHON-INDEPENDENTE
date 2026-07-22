#Atendente de um escola de música
from random import randint
from random import choice

palavras = {
    'saudacoes': [
        'oi',
        'olá',
        'ola',
        'e aí',
        'e ai',
        'opa',
        'iae',
        'salve',
        'fala',
        'bom dia',
        'boa tarde',
        'boa noite',
        'tudo bem',
        'tudo bom',
        'beleza',
        'tranquilo',
        'hey',
        'hello',
        'hi',
        'oii'
    ],

    'despedidas': [
        'tchau',
        'até logo',
        'ate logo',
        'até mais',
        'ate mais',
        'falou',
        'fui',
        'até',
        'ate',
        'xau',
        'bye',
        'goodbye'
    ]
}
while True:
    saudacao = input(f"{choice(palavras['saudacoes'])}\n").strip().lower()
    if saudacao in palavras['saudacoes']:
        print('como posso ajudar?')
    elif saudacao in palavras['despedidas']:
        print(choice(palavras['despedidas']))
    else:
        print('Desculpe, não entendi o que você quis dizer.')