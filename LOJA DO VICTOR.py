print('=' * 30)
print(f'{" LOJA DO VICTOR ":^30}')
print('=' * 30)

produtos = [
        {"nome": "Mouse", "preco": 80},
        {"nome": "Teclado", "preco": 150},
        {"nome": "Headset", "preco": 200},
        {"nome": "Monitor", "preco": 900}
        ]

carrinho = []

while True:
    print('-' * 30)
    print('''[0] Sair
    [1] Ver produtos
    [2] Comprar produtos
    [3] Ver carrinho
    [4] Finalizar compra''')
    while True:
        escolha = int(input('O que gostaria de fazer? '))
        if 0 <= escolha <= 4:
            break
        print('Opção inválida! Escolha o que fazer agora: ')
    print('-' * 30)

#SAIR
    if escolha == 0:
        print('Saindo...')
        break

#VER PRODUTOS
    elif escolha == 1:
        print('Produtos: ')
        for codigo, produto in enumerate(produtos):
            print(f'Código: {codigo} - Produto: {produto["nome"]} - R${produto["preco"]}')
        print('-' * 30)

#COMPRAR PRODUTOS
    elif escolha == 2:
        while True:
            while True:
                interesse = int(input('Código do produto que deseja comprar: '))
                if 0 <= interesse < len(produtos):
                    carrinho.append(produtos[interesse])
                    break
                print('Código inválido.')
            continuar = input('Deseja adicionar mais produtos ao carrinho? [S/N]').strip().upper()[0]
            if continuar == 'N':
                break
        print('-' * 30)

#VER CARRINHO
    elif escolha == 3:
        print('CARRINHO: ')
        if not carrinho:
            print('O carrinho está vazio.')
        else:
            for produto in carrinho:
                print(f'Produto: {produto["nome"]} - R${produto["preco"]}')

#FINALIZAR COMPRA
    elif escolha == 4:
        if not carrinho:
            print('O carrinho está vazio. Saindo...')
        else:
            total_compra = 0
            for produto in carrinho:
                total_compra += produto['preco']
                print(f'Produto: {produto["nome"]} - R${produto["preco"]}')
                print('-' * 30)
            print(f'Total da compra de R${total_compra}')
            print('Finalizando compra...')
        break