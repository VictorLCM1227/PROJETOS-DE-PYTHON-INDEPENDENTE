def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
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
            print('\033[31mERRO: digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


def leiaFloatPositivo(msg):
    while True:
        numero = leiaFloat(msg)

        if numero > 0:
            return numero

        print('\033[31mERRO: digite um número maior que zero.\033[m')


def linha(simbolo='-', tam=60):
    return simbolo * tam


def cabecalho(txt, simbolo='-'):
    print()
    print(linha(simbolo))
    print(txt.center(60))
    print(linha(simbolo))


def menu(lista, menu_msg='MENU PRINCIPAL'):
    cabecalho(menu_msg)

    for indice, item in enumerate(lista):
        print(f'\033[33m[{indice}]\033[m - \033[34m{item}\033[m')

    print(linha())

    return leiaInt('\033[32mSua opção: \033[m')


def existe_gastos():
    if not gastos:
        print('Ainda não há gastos registrados.')
        return False

    return True


def mostrar_gasto(gasto):
    print(
        f"{'ID':<5}"
        f"{'Descrição':<25}"
        f"{'Valor':<15}"
        f"{'Categoria':<15}"
    )

    print(
        f"{gasto['id']:<5}"
        f"{gasto['descricao']:<25}"
        f"R${gasto['valor']:<13.2f}"
        f"{gasto['categoria']:<15}"
    )


def categoria():
    while True:

        opcao = menu(
            categorias,
            menu_msg='CATEGORIAS DO GASTO'
        )

        if 0 <= opcao < len(categorias):
            return categorias[opcao]

        print('\033[31mOpção inválida.\033[m')


def adicionar_gasto():
    global proximo_id

    gasto = {}

    gasto['id'] = proximo_id

    while True:
        descricao = input('Descrição: ').strip()

        if descricao:
            break

        print('\033[31mERRO: a descrição não pode ficar vazia.\033[m')

    gasto['descricao'] = descricao

    gasto['valor'] = leiaFloatPositivo(
        'Valor: R$ '
    )

    gasto['categoria'] = categoria()

    gastos.append(gasto)

    proximo_id += 1

    print('\033[32mGasto cadastrado com sucesso!\033[m')


def listar_gastos():
    if not existe_gastos():
        return

    print(
        f"{'ID':<5}"
        f"{'Descrição':<25}"
        f"{'Valor':<15}"
        f"{'Categoria':<15}"
    )

    print(linha())

    for gasto in gastos:
        print(
            f"{gasto['id']:<5}"
            f"{gasto['descricao']:<25}"
            f"R${gasto['valor']:<13.2f}"
            f"{gasto['categoria']:<15}"
        )


def calcular_total():
    total = 0

    for gasto in gastos:
        total += gasto['valor']

    return total


def ver_total_gasto():
    if not existe_gastos():
        return

    total = calcular_total()

    print(f'Total gasto: R$ {total:.2f}')


def media_dos_gastos():
    if not existe_gastos():
        return

    total = calcular_total()

    media = total / len(gastos)

    print(f'Média dos gastos: R$ {media:.2f}')


def encontrar_maior_gasto():
    maior = gastos[0]

    for gasto in gastos:
        if gasto['valor'] > maior['valor']:
            maior = gasto

    return maior


def encontrar_menor_gasto():
    menor = gastos[0]

    for gasto in gastos:
        if gasto['valor'] < menor['valor']:
            menor = gasto

    return menor


def maior_gasto():
    if not existe_gastos():
        return

    maior = encontrar_maior_gasto()

    print('Maior gasto:')
    print(linha())

    mostrar_gasto(maior)


def menor_gasto():
    if not existe_gastos():
        return

    menor = encontrar_menor_gasto()

    print('Menor gasto:')
    print(linha())

    mostrar_gasto(menor)


def gastos_por_categoria():
    if not existe_gastos():
        return

    print(
        f"{'Categoria':<20}"
        f"{'Total':<15}"
    )

    print(linha())

    for categoria_atual in categorias:

        total = 0

        for gasto in gastos:
            if gasto['categoria'] == categoria_atual:
                total += gasto['valor']

        print(
            f"{categoria_atual:<20}"
            f"R$ {total:.2f}"
        )


# ====================================
# PROGRAMA PRINCIPAL
# ====================================

gastos = []

categorias = [
    'alimentacao',
    'transporte',
    'lazer',
    'educacao',
    'saude',
    'outros'
]

proximo_id = 1


while True:

    opcao = menu(
        [
            'Sair',
            'Adicionar gasto',
            'Listar gastos',
            'Ver total gasto',
            'Ver gastos por categoria',
            'Maior gasto',
            'Média dos gastos',
            'Menor gasto'
        ],
        menu_msg='CONTROLE FINANCEIRO'
    )

    if opcao == 0:
        cabecalho('SAINDO')
        print('Até logo!')
        break

    elif opcao == 1:
        cabecalho('ADICIONAR GASTO')
        adicionar_gasto()

    elif opcao == 2:
        cabecalho('LISTAR GASTOS')
        listar_gastos()

    elif opcao == 3:
        cabecalho('TOTAL GASTO')
        ver_total_gasto()

    elif opcao == 4:
        cabecalho('GASTOS POR CATEGORIA')
        gastos_por_categoria()

    elif opcao == 5:
        cabecalho('MAIOR GASTO')
        maior_gasto()

    elif opcao == 6:
        cabecalho('MÉDIA DOS GASTOS')
        media_dos_gastos()

    elif opcao == 7:
        cabecalho('MENOR GASTO')
        menor_gasto()

    else:
        print('\033[31mOpção inválida.\033[m')