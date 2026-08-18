from time import sleep

tarefas = []
tarefas_concluidas = []


# ==============================
# FUNÇÕES DE INTERFACE
# ==============================

def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print()
    print(linha())
    print(txt.center(50))
    print(linha())


def pausa():
    sleep(1)


# ==============================
# FUNÇÕES DE ENTRADA
# ==============================

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except ValueError:
            print('\033[31mERRO: digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mOperação cancelada pelo usuário.\033[m')
            return 0


# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def existe_conteudo(lista, msg='Ainda não há tarefas.'):
    if not lista:
        print(msg)
        return False

    return True


def mostrar_tarefas(lista):
    for indice, tarefa in enumerate(lista):
        print(f'\033[33m[{indice}]\033[m - \033[34m{tarefa}\033[m')


# ==============================
# MENU
# ==============================

def menu(lista):
    cabecalho('TO DO LIST')

    for indice, item in enumerate(lista):
        print(f'\033[33m[{indice}]\033[m - \033[34m{item}\033[m')

    print(linha())

    return leiaInt('\033[32mSua opção: \033[m')


# ==============================
# TAREFAS
# ==============================

def adicionar_tarefa():
    cabecalho('ADICIONAR TAREFA')

    tarefa = input('Digite a nova tarefa: ').strip()

    if not tarefa:
        print('\033[31mERRO: digite uma tarefa válida.\033[m')
        return

    tarefas.append(tarefa)

    print('\033[32mTarefa adicionada com sucesso!\033[m')


def listar_tarefas():
    cabecalho('TAREFAS PENDENTES')

    if existe_conteudo(tarefas):
        mostrar_tarefas(tarefas)


def concluir_tarefa():
    cabecalho('CONCLUIR TAREFA')

    if not existe_conteudo(tarefas):
        return

    mostrar_tarefas(tarefas)

    indice = leiaInt('\nDigite o número da tarefa concluída: ')

    try:
        tarefa = tarefas[indice]
        tarefas_concluidas.append(tarefa)
        del tarefas[indice]

        print('\033[32mTarefa concluída com sucesso!\033[m')

    except IndexError:
        print('\033[31mERRO: o índice digitado não existe.\033[m')


def remover_tarefa():
    cabecalho('REMOVER TAREFA')

    if not existe_conteudo(tarefas):
        return

    mostrar_tarefas(tarefas)

    indice = leiaInt('\nDigite o número da tarefa a ser removida: ')

    try:
        tarefa = tarefas[indice]
        del tarefas[indice]

        print(f'\033[32mTarefa "{tarefa}" removida com sucesso!\033[m')

    except IndexError:
        print('\033[31mERRO: o índice digitado não existe.\033[m')


def listar_tarefas_concluidas():
    cabecalho('TAREFAS CONCLUÍDAS')

    if existe_conteudo(
        tarefas_concluidas,
        'Ainda não há tarefas concluídas.'
    ):
        mostrar_tarefas(tarefas_concluidas)


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

opcoes = [
    'SAIR',
    'ADICIONAR TAREFA',
    'LISTAR TAREFAS',
    'CONCLUIR TAREFA',
    'REMOVER TAREFA',
    'LISTAR TAREFAS CONCLUÍDAS'
]


while True:

    opcao = menu(opcoes)

    if opcao == 0:
        cabecalho('SAINDO...')
        print('Até logo!')
        break

    elif opcao == 1:
        adicionar_tarefa()

    elif opcao == 2:
        listar_tarefas()

    elif opcao == 3:
        concluir_tarefa()

    elif opcao == 4:
        remover_tarefa()

    elif opcao == 5:
        listar_tarefas_concluidas()

    else:
        cabecalho('ERRO')
        print('\033[31mDigite uma opção válida!\033[m')

    pausa()