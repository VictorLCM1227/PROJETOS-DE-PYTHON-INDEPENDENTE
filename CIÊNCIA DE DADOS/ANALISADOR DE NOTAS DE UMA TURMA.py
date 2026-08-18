alunos = []


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


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero

        except ValueError:
            print('\033[31mERRO: digite um número real válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mOperação cancelada pelo usuário.\033[m')
            return 0


# ==============================
# INTERFACE
# ==============================

def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print()
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for indice, item in enumerate(lista):
        print(f'\033[33m[{indice}]\033[m - \033[34m{item}\033[m')

    print(linha())

    return leiaInt('\033[32mSua opção: \033[m')


# ==============================
# CADASTRO
# ==============================

def cadastrar_aluno():
    aluno = {}

    nome = input('Nome do aluno: ').strip().upper()

    while not nome:
        print('\033[31mERRO: o nome não pode ficar vazio.\033[m')
        nome = input('Nome do aluno: ').strip().upper()

    aluno['NOME'] = nome

    notas = []
    contador = 1

    while True:

        nota = leiaFloat(f'{contador}ª nota: ')

        while nota < 0 or nota > 10:
            print('\033[31mERRO: a nota deve estar entre 0 e 10.\033[m')
            nota = leiaFloat(f'{contador}ª nota: ')

        notas.append(nota)
        contador += 1

        while True:
            continuar = input(
                'Quer adicionar outra nota? [S/N] '
            ).strip().upper()

            if continuar and continuar[0] in 'SN':
                break

            print('\033[31mOpção inválida. Digite S ou N.\033[m')

        if continuar[0] == 'N':
            break

    aluno['NOTAS'] = notas

    alunos.append(aluno)

    print('\033[32mAluno cadastrado com sucesso!\033[m')


# ==============================
# EXIBIÇÃO
# ==============================

def mostrar_alunos():
    if not alunos:
        print('Nenhum aluno cadastrado.')
        return

    for indice, aluno in enumerate(alunos, start=1):
        print(f'ALUNO {indice}')

        print(f'NOME: {aluno["NOME"]}')
        print(f'NOTAS: {aluno["NOTAS"]}')

        print(linha())


# ==============================
# MÉDIAS
# ==============================

def calcular_media(aluno):
    return sum(aluno['NOTAS']) / len(aluno['NOTAS'])


def calcular_medias(mostrar=True):
    if not alunos:
        print('Nenhum aluno cadastrado.')
        return

    for aluno in alunos:

        media = calcular_media(aluno)

        if mostrar:
            print(f'NOME: {aluno["NOME"]}')
            print(f'MÉDIA: {media:.2f}')

            if media >= 7:
                print('SITUAÇÃO: \033[32mAPROVADO\033[m')
            else:
                print('SITUAÇÃO: \033[31mREPROVADO\033[m')

            print(linha())


# ==============================
# ESTATÍSTICAS
# ==============================

def estatisticas_da_turma():
    if not alunos:
        print('Nenhum aluno cadastrado.')
        return

    quantidade_alunos = len(alunos)

    maior_media = 0
    menor_media = 0
    soma_medias = 0
    aprovados = 0
    reprovados = 0

    for contador, aluno in enumerate(alunos):

        media = calcular_media(aluno)

        soma_medias += media

        if media >= 7:
            aprovados += 1
        else:
            reprovados += 1

        if contador == 0:
            maior_media = media
            menor_media = media
        else:
            if media > maior_media:
                maior_media = media

            if media < menor_media:
                menor_media = media

    media_geral = soma_medias / quantidade_alunos

    print(f'Quantidade de alunos: {quantidade_alunos}')
    print(f'Maior média: {maior_media:.2f}')
    print(f'Menor média: {menor_media:.2f}')
    print(f'Média geral da turma: {media_geral:.2f}')
    print(f'Quantidade de aprovados: {aprovados}')
    print(f'Quantidade de reprovados: {reprovados}')


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

opcoes = [
    'Sair',
    'Cadastrar aluno',
    'Mostrar alunos',
    'Ver médias',
    'Estatísticas da turma'
]


while True:

    opcao = menu(opcoes)

    if opcao == 0:
        cabecalho('SAINDO...')
        print('Até logo!')
        break

    elif opcao == 1:
        cabecalho('CADASTRAR ALUNO')
        cadastrar_aluno()

    elif opcao == 2:
        cabecalho('MOSTRAR ALUNOS')
        mostrar_alunos()

    elif opcao == 3:
        cabecalho('VER MÉDIAS')
        calcular_medias()

    elif opcao == 4:
        cabecalho('ESTATÍSTICAS DA TURMA')
        estatisticas_da_turma()

    else:
        cabecalho('ERRO')
        print('\033[31mDigite uma opção válida!\033[m')