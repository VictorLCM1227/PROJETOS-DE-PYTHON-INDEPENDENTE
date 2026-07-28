
def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
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
        except ValueError:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero

def leiaFloatPositivo(msg):
    while True:
        try:
            numero = float(input(msg))    
        except ValueError:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            if numero > 0:
                return numero
            print('\033[31mERRO: por favor, digite um número real válido e maior do que zero.\033[m')

def linha(simbolo='-', tam=42):
    return simbolo * tam 

def cabecalho(txt, simbolo='-'):
    print(linha(simbolo))
    print(txt.center(42))
    print(linha(simbolo))

def menu(lista, menu_msg='MENU PRINCIPAL'):
    cabecalho(menu_msg)
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

gastos = []
categorias = ['alimentacao', 'transporte', 'lazer', 'educacao', 'saude', 'outros']
proximo_id = 1

def categoria():
    while True:
        categoria = menu(categorias, menu_msg='CATEGORIAS DO GASTO')
        if 0 <= categoria <= len(categorias) - 1:
            break
        print('Opção inválida.')
    return categorias[categoria]
    


def adicionar_gasto():
    global proximo_id
    gasto = {}
    gasto['id'] = proximo_id
    gasto['descricao'] = input('Descrição: ')
    gasto['valor'] = leiaFloatPositivo('Valor: R$')
    gasto['categoria'] = categoria()
    gastos.append(gasto)
    proximo_id += 1

def listar_gastos():
    if not gastos:
        print('Nenhum gasto cadastrado.')
    else:
        print(f'{"ID":<4}{"Descrição":<20} {"Valor":<12} {"Categoria":<12}')
        print(linha())
        for gasto in gastos:
            print(f"{gasto['id']:<4} {gasto['descricao']:<20} {gasto['valor']:<12.2f} {gasto['categoria']:<12}")

def ver_total_gasto(devolver=False, mostrar=True):
    total = 0
    for gasto in gastos:
        total += gasto['valor']
    if mostrar:
        print(f'O total gasto foi R${total:.2f}')
    if devolver:
        return total

def media_dos_gastos():
    if not gastos:
        print('Ainda não há gastos registrados.')
    else:
        total = ver_total_gasto(devolver=True, mostrar=False)
        media = total / len(gastos)
        print(f'A média dos gastos é R${media:.2f}')

def maior_gasto():
    if not gastos:
        print('Ainda não há gastos registrados.')
    else:
        maior = gastos[0]
        for gasto in gastos:
            if gasto['valor'] > maior['valor']:
                maior = gasto
        print(f'{"ID":<4}{"Descrição":<20} {"Valor":<12} {"Categoria":<12}')
        print(f"{maior['id']:<4} {maior['descricao']:<20} {maior['valor']:<12.2f} {maior['categoria']:<12}")

def menor_gasto():
    if not gastos:
        print('Ainda não há gastos registrados.')
    else:
        menor = gastos[0]
        for gasto in gastos:
            if gasto['valor'] < menor['valor']:
                menor = gasto
        print(f'{"ID":<4}{"Descrição":<20} {"Valor":<12} {"Categoria":<12}')
        print(f"{menor['id']:<4} {menor['descricao']:<20} {menor['valor']:<12.2f} {menor['categoria']:<12}")

def gastos_por_categoria():
    if not gastos:
        print('Ainda não há gastos registrados.')
    else:
        print(f'{"Categoria":<15} {"Total":<15}')
        print(linha())
        for categoria_atual in categorias:
            total = 0
            for gasto in gastos:
                if gasto['categoria'] == categoria_atual:
                    total += gasto['valor']
            print(f'{categoria_atual:<15} : R${total:<15.2f}')

while True:
    opcao = menu(['Sair', 'Adicionar gasto', 'Listar gastos', 'Ver total gasto',
                   'Ver gastos por categoria', 'Maior gasto', 'Média dos gastos', 'Menor gasto'], menu_msg='CONTROLE FINANCEIRO')

    if opcao == 0:
        cabecalho('Saindo')
        break
    elif opcao == 1:
        cabecalho('Adicionar gasto')
        adicionar_gasto()
        
    elif opcao == 2:
        cabecalho('Listar gastos')
        listar_gastos()
        
    elif opcao == 3:
        cabecalho('Ver total gasto')
        ver_total_gasto()

    elif opcao == 4:
        cabecalho('Ver gastos por categoria')
        gastos_por_categoria()

    elif opcao == 5:
        cabecalho('Maior gasto')
        maior_gasto()

    elif opcao == 6:
        cabecalho('Média dos gastos')
        media_dos_gastos()

    elif opcao == 7:
        cabecalho('Menor gasto')
        menor_gasto()

    else:
        print('Opção inválida.')
        
