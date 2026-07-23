from random import choice
from time import sleep

def pergunta_resposta():
    for tema, palavras in palavras_chave.items():
        for palavra in palavras:
            if voce == palavra:
                chat = tema
                return chat

palavras_chave = {
    'saudações' : ['oi'],
    'despedidas' : ['tchau']
}

resposta = {
    'saudações': ['Opa, Bão?', 'Eai! Blz?'],
    'despedidas':['Tcahu! Volte sempre!', 'Falou mano!']
}

while True:
    voce = input('você: ').strip().lower()
    chat = pergunta_resposta()
    if chat != '':
        print(f'CHAT: {choice(resposta[chat])}')
        sleep(1)
        if chat == 'despedidas':
            break
        