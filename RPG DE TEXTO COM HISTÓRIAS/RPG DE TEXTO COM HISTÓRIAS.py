print('=' * 50)
print(f'{" BEM VINDO AO RPG DE TEXTO COM HÍSTORIAS ":^50}')
print('=' * 50)

print('Escolha uma hisória para jogar:')
print('''[0] Sair
[1]''')
historia_escolhida = int(input('>>>Qual a sua escolha? '))

if historia_escolhida == 0:
    print('Saindo...')
if historia_escolhida == 1:
    print('Você escolheu a história:')