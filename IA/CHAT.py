#CHAT
from random import choice
from time import sleep
import FUNCOES


FUNCOES.cabeçalho('CHAT BOT SIMPLES')
print(f'\033[32mCHAT: Bem Vindo(a)! Prazer em te conhecer!\033[m')

while True:
    resposta_menu = FUNCOES.menu(['Sair', 'Conversar'])
    if resposta_menu == 0:
        FUNCOES.cabeçalho('Saindo do Sistema... Até logo!')
        break
    if resposta_menu == 1:
        FUNCOES.cabeçalho('CONVERSANDO')
        while True:
            voce = input('\033[34mvocê: \033[m').strip().lower()
            categoria = FUNCOES.pergunta_resposta(voce)
            print(f'\033[32mCHAT: {choice(FUNCOES.respostas[categoria])}\033[m')
            sleep(1)
            if categoria == 'despedidas':
                break
    else:
        FUNCOES.cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    


'''
Coisas pra fazer
0 sair
1 conversar
2 pedir pro chat fazer contas (importar calculadora)
2 funcoespro chat
mais palavras chave
'''
