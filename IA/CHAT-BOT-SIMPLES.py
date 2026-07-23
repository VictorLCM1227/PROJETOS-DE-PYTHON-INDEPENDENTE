#Atendente de um escola de música
from random import choice


palavras_chave = {
    'saudacoes': [
        'oi', 'olá', 'ola', 'bom dia', 'boa tarde',
        'boa noite', 'opa', 'e ai', 'e aí'
    ],

    'despedidas': [
        'tchau', 'até logo', 'ate logo', 'falou',
        'bye', 'goodbye'
    ],

    'preco': [
        'preço', 'preco', 'valor', 'quanto custa',
        'mensalidade'
    ],

    'horario': [
        'horário', 'horario', 'funcionamento',
        'abre', 'fecha'
    ],

    'cursos': [
        'curso', 'cursos', 'aulas',
        'violão', 'guitarra', 'piano',
        'bateria', 'canto'
    ]
}

palavras_chave = {
    'saudacoes': [...],
    'despedidas': [...],
    'cursos': [
        'cursos',
        'curso',
        'aulas',
        'violão',
        'violao',
        'guitarra',
        'piano'
    ],
    'precos': [
        'preço',
        'preco',
        'valor',
        'mensalidade'
    ]
}

respostas = {
    'saudacoes': [...],
    'despedidas': [...],
    'cursos': [
        'Temos aulas de violão, guitarra, piano, bateria e canto.'
    ],
    'precos': [
        'As mensalidades variam conforme o curso. Deseja saber o valor de qual instrumento?'
    ]
}





while True:
    mensagem = input('VOCÊ: ').strip().lower()
    for categoria in palavras_chave:
        if mensagem in palavras_chave[categoria]:
            print(f'CHAT: {choice(respostas["categoria"])}')
            break