#perfil
from utilidades import leiaInt, linha, cabeçalho, menu

def mostrar_perfil(nome='<DESCONHECIDO>', saldo=0, jogos_jogados=0):
    cabeçalho('PERFIL')
    print(f'Nome: {nome}')
    print(f'Saldo: R${saldo}')
    print(f'Jogos jogados: {jogos_jogados}')
    print('[0] VOLTAR')