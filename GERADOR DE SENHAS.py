from random import randint
print('=' * 50)
print(f'{" BEM-VINDO(A) AO GERADOR DE SENHAS DO VICTOR! ":^50}')
print('=' * 50)
tamanho_da_senha = int(input('Tamanho da senha: '))
numeros = input('Terá números? [S/N] ').strip().upper()[0]
simbolos = input('Digite os símbolos que gostaria que tivesse: ')