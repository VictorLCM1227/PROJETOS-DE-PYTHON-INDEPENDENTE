
alunos = []

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

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

def cadastrar_aluno():
    aluno = {}
    aluno['NOME'] = input('Nome do Aluno: ').strip().upper()
    notas = []
    contador = 1
    while True:
        notas.append(leiaFloat(f'{contador}ª nota: '))
        contador += 1
        while True:
            continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
            if continuar in 'SN':
                break
            print('Opção inválida.')
        if continuar == 'N':
            break
    aluno['NOTAS'] = notas
    alunos.append(aluno)
    
def mostrar_alunos():
    if not alunos:
        print('Nenhum aluno cadastrado.')
    else:
        for aluno in alunos:
            for chave, valor in aluno.items():
                print(f'{chave}: {valor}')
            print(linha())

def calcular_medias(mostrar=True):
    global menor_media, maior_media, medias, aprovados, reprovados
    if not alunos:
        print('Nenhum aluno cadastrado.')
    else:
        medias = aprovados = reprovados = contador = 0
        for aluno in alunos:
            contador += 1
            media = sum(aluno['NOTAS']) / len(aluno["NOTAS"])
            if mostrar:
                print(f'NOME: {aluno["NOME"]}')
                print(f'MÉDIA: {media:.2f}')
                print(linha())
            if contador == 1:
                maior_media = menor_media = media
            else:
                if media > maior_media:
                    maior_media = media
                if media < menor_media:
                    menor_media = media
            medias += media
            if media >= 7:
                aprovados += 1
            else:
                reprovados += 1
            
def estatisticas_da_turma():
    if not alunos:
            print('Nenhum aluno cadastrado.')
    else:
        quantidade_de_alunos = len(alunos)
        print(f'A quantidade de alunos cadastrados é {quantidade_de_alunos}')
        calcular_medias(mostrar=False)
        print(f'A maior média foi {maior_media:.2f}')
        print(f'A menor média foi {menor_media:.2f}')
        print(f'A média geral da turma foi {medias / quantidade_de_alunos}')
        print(f'A quantidade de aprovados é {aprovados}')
        print(f'A quantidade de reprovados é {reprovados}')

while True:
    cabecalho('ANALISADOR DE NOTAS')
    opcao = menu(['Sair', 'Cadastrar aluno', 'Mostrar alunos', 'Ver médias', 'Estatísticas da turma'])
    if opcao == 0:
        cabecalho('SAINDO...')
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
        cabecalho('ESTATÍSTICA DA TURMA')
        estatisticas_da_turma()