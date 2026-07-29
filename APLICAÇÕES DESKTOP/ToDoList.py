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

def verifica_se_vazio(variavel, msg='Ainda não há tarefas.'):
    if not variavel:
        print(msg)
    else:
        return True

def mostrar_tarefas(variavel):
    for indice, tarefa in enumerate(variavel):
        print(f'{indice} - {tarefa}')
    
def adicionar_tarefa():
    cabeçalho('ADICIONAR TAREFA')
    tarefa = input('Digite a nova tarefa: ').strip()
    if verifica_se_vazio(tarefa, msg='Não foi digitado uma tarefa válida.'):
        tarefas.append(tarefa)

def listar_tarefas():
    cabeçalho('LISTAR TAREFAS')
    if verifica_se_vazio(tarefas):
        mostrar_tarefas(tarefas)

def concluir_remover_tarefas(msg_cabecalho='REMOVER TAREFA', salvar_concluida=False, msg_acao='Digite o número da tarefa a ser removida '):
    cabeçalho(msg_cabecalho)
    if verifica_se_vazio(tarefas):
        mostrar_tarefas(tarefas)
        acao = leiaInt(msg_acao)
        try:
            if salvar_concluida:
                tarefas_concluidas.append(tarefas[acao])
            del tarefas[acao]
        except IndexError:
            print('\033[31mO indice digitado não existe.\033[m')

def listar_tarefas_concluidas():
    cabeçalho('LISTAR TAREFAS CONCLUÍDAS')
    if verifica_se_vazio(tarefas_concluidas):
        mostrar_tarefas(tarefas_concluidas)
while True:
    opcao = menu(['SAIR', 'ADICIONAR TAREFA', 'LISTAR TAREFAS', 'CONCLUIR TAREFAS', 'REMOVER TAREFA',
                  'LISTAR TAREFAS CONCLUÍDAS'])
    if opcao == 0:
        cabeçalho('SAINDO...')
        break
    elif opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        concluir_remover_tarefas(msg_cabecalho='CONCLUIR TAREFAS', salvar_concluida=True, msg_acao='Digite o número da tarefa concluída: ')
    elif opcao == 4:
        concluir_remover_tarefas()
    elif opcao == 5:
        listar_tarefas_concluidas()
    sleep(1)