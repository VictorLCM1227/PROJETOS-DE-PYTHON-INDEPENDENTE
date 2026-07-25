from time import sleep

tarefas = []
tarefas_concluidas = []

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número interiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

def linha(tam = 42):
    return '-' * tam 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('TO DO LIST')
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao


while True:
    opcao = menu(['SAIR', 'ADICIONAR TAREFA', 'LISTAR TAREFAS', 'CONCLUIR TAREFAS', 'REMOVER TAREFA',
                  'LISTAR TAREFAS CONCLUÍDAS.'])
    if opcao == 0:
        cabeçalho('SAINDO...')
        break
    elif opcao == 1:
        cabeçalho('ADICIONAR TAREFA')
        tarefa = input('Digite a nova tarefa: ').strip()
        tarefas.append(tarefa)
    elif opcao == 2:
        cabeçalho('LISTAR TAREFAS')
        if not tarefas:
            print('Ainda não há tarefas.')
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f'{indice} - {tarefa}')
    elif opcao == 3:
        cabeçalho('CONCLUIR TAREFAS')
        if not tarefas:
            print('Ainda não há tarefas.')
        else:
            concluir = leiaInt('Digite o número da tarefa concluída: ')
            try:
                tarefas_concluidas.append(tarefas[concluir])
                del tarefas[concluir]
            except IndexError:
                print('\033[31mO indice digitado não existe.\033[m')
    elif opcao == 4:
        cabeçalho('REMOVER TAREFA')
        if not tarefas:
            print('Ainda não há tarefas.')
        else:
            remover = leiaInt('Digite o número tarefa a ser removida: ')
            try:
                del tarefas[remover]
            except IndexError:
                print('\033[31mO indice digitado não existe.\033[m')
    elif opcao == 5:
        cabeçalho('LISTAR TAREFAS CONCLUÍDAS')
        if not tarefas:
            print('Ainda não há tarefas concluídas.')
        else:
            for indice, tarefa in enumerate(tarefas_concluidas):
                print(f'{indice} - {tarefa}')
    sleep(1)