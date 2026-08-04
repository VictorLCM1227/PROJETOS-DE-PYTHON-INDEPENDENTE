#carteira

from utilidades import leiaInt, linha, cabeçalho, menu, leiaFloatPositivo
from time import sleep

def depositar(saldo, extrato):
    while True:
        deposito = leiaFloatPositivo(input('Valor do depósito: R$'))
        if deposito < 1:
            print('O valor do depósito deve ser maior que zero.')
        else:
            print('Depositando...')
            sleep(0.5)
            saldo += deposito
            extrato.append(('Depósito',deposito))
            return saldo, extrato

def sacar(saldo, extrato):
    while True:
        saque = leiaFloatPositivo(input('Valor do Saque: R$'))
        if saque < 1:
            print('O valor do saque deve ser maior que zero.')
        else:
            if saque > saldo:
                print('Saldo Insuficiente.')
            else:
                print('Sacando...')
                sleep(0.5)
                extrato.append(('Saque',saque * (-1)))
                saldo -= saque
                cedula = 200
                cedula_quantidade = 0
                while True:
                    if saque >= cedula:
                        saque -= cedula
                        cedula_quantidade += 1
                    else:
                        if cedula_quantidade > 0:
                            print(f'Total de {cedula_quantidade} cédulas de R${cedula}')
                        if cedula == 200:
                            cedula = 100
                        elif cedula == 100:
                            cedula = 50
                        elif cedula == 50:
                            cedula = 20
                        elif cedula == 20:
                            cedula = 10
                        elif cedula == 10:
                            cedula = 5
                        elif cedula == 5:
                            cedula = 1
                        cedula_quantidade = 0
                        if saque == 0:
                            break
                return saldo, extrato

def mostrar_extrato(extrato, saldo):
    print('Abrindo extrato:')
    sleep(0.5)
    if not extrato:
        print('Ainda não houve Transações.')
    else:
        for descricao, valor in extrato:
            if valor >= 0:
                sinal = '+'
            else:
                sinal = '-'
            print(f'{descricao:<25} {sinal}R${abs(valor):.2f}')
        print(linha())
        print(f'Saldo atual: R${saldo}')
    

#se o saldo for insuficiente, a função retorna none
def validar_aposta(saldo):
    if saldo < 1:
        print('Saldo insuficiente.')
    else:
        while True:
            aposta = leiaFloatPositivo('Quanto deseja apostar? R$')
            if aposta <= saldo:
                return aposta
            print('A sua aposta só pode ser menor ou igual ao seu saldo.')

def atualizar_aposta(ficha_do_jogador, aposta, resultado, jogo):
    if aposta > ficha_do_jogador['carteira']['maior_aposta_feita']:
        ficha_do_jogador['carteira']['maior_aposta_feita'] = aposta
    if aposta > ficha_do_jogador['estatisticas_jogos'][jogo]['maior_aposta']:
            ficha_do_jogador['estatisticas_jogos'][jogo]['maior_aposta'] = aposta
    if resultado == 'V':
        ficha_do_jogador['estatisticas_gerais']['vitorias_totais'] += 1
        ficha_do_jogador['carteira']['saldo'] += aposta * 2
        ficha_do_jogador['extrato'].append((f'Vitória {jogo}', aposta * 2))
        ficha_do_jogador['estatisticas_gerais']['dinheiro_ganho_total'] += aposta
        ficha_do_jogador['estatisticas_jogos'][jogo]['dinheiro_ganho'] += aposta 
        ficha_do_jogador['estatisticas_jogos'][jogo]['sequencia_atual'] += 1
        if ficha_do_jogador['estatisticas_jogos'][jogo]['sequencia_atual'] > ficha_do_jogador['estatisticas_jogos'][jogo]['melhor_sequencia']:
            ficha_do_jogador['estatisticas_jogos'][jogo]['melhor_sequencia'] = ficha_do_jogador['estatisticas_jogos'][jogo]['sequencia_atual']

        ficha_do_jogador['estatisticas_jogos'][jogo]['vitorias'] += 1
    elif resultado == 'D':
        ficha_do_jogador['estatisticas_gerais']['derrotas_totais'] += 1
        ficha_do_jogador['estatisticas_gerais']['dinheiro_perdido_total'] += aposta
        ficha_do_jogador['estatisticas_jogos'][jogo]['derrotas'] += 1
        ficha_do_jogador['estatisticas_jogos'][jogo]['dinheiro_perdido'] += aposta
        ficha_do_jogador['estatisticas_jogos'][jogo]['sequencia_atual'] = 0
    elif resultado == 'E':
        ficha_do_jogador['estatisticas_gerais']['empates_totais'] += 1
        ficha_do_jogador['carteira']['saldo'] += aposta
        ficha_do_jogador['extrato'].append((f'Empate {jogo}', aposta))
        ficha_do_jogador['estatisticas_jogos'][jogo]['empates'] += 1
        ficha_do_jogador['estatisticas_jogos'][jogo]['sequencia_atual'] = 0
