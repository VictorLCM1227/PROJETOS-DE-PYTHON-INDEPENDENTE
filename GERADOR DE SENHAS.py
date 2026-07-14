from random import randint
print('=' * 50)
print(f'{" BEM-VINDO(A) AO GERADOR DE SENHAS DO VICTOR! ":^50}')
print('=' * 50)
tamanho_da_senha = int(input('Tamanho da senha: '))
se_numeros = input('Terá Números? [S/N] ').strip().upper()[0]
se_letras_maiusculas = input('Terá Letras Maiúsculas? [S/N] ').strip().upper()[0]
se_letras_minusculas = input('Terá Letras Minúsculas? [S/N] ').strip().upper()[0]
se_caracteres_especiais = input('Terá Caracteres Especiais? [S/N] ').strip().upper()[0]
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
letras_maiusculas = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

letras_minusculas = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

caracteres_especiais = [
    '!', '@', '#', '$', '%',
    '&', '*', '-', '_',
    '+', '=', '?'
]