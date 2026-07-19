from random import randint
import random

print('=' * 50)
print(f'{" BEM-VINDO(A) AO GERADOR DE SENHAS DO VICTOR! ":^50}')
print('=' * 50)

limite = tamanho_da_senha = int(input('Tamanho da senha: '))

while True:
    se_numeros = input('Terá Números? [S/N] ').strip().upper()[0]
    if se_numeros in 'SN':
        break
    print('Opção inválida.')
if se_numeros == 'S':
    while True:
        quantidade_numeros = int(input('Quantos números? '))
        if quantidade_numeros <= limite:
            limite = limite - quantidade_numeros
            break
        print('A quantidade de números é superior a quantidade de caracteres disponíveis para a senha.')
else: 
    quantidade_numeros = 0

while True:
    se_letras_maiusculas = input('Terá Letras Maiúsculas? [S/N] ').strip().upper()[0]
    if se_letras_maiusculas in 'SN':
        break
    print('Opção inválida.')
if se_letras_maiusculas == 'S':
    while True:
        quantidade_letras_maiusculas = int(input('Quantas Letras Maiúsculas? '))
        if quantidade_letras_maiusculas <= limite:
            limite = limite - quantidade_letras_maiusculas
            break
        print('A quantidade de letras maiúsculas é superior a quantidade de caracteres disponíveis para a senha.')
else: 
    quantidade_letras_maiusculas = 0

while True:
    se_letras_minusculas = input('Terá Letras Minúsculas? [S/N] ').strip().upper()[0]
    if se_letras_minusculas in 'SN':
        break
    print('Opção inválida.')
if se_letras_minusculas == 'S':
    while True:
        quantidade_letras_minusculas = int(input('Quantas Letras Minúsculas? '))
        if quantidade_letras_minusculas <= limite:
            limite = limite - quantidade_letras_minusculas
            break
        print('A quantidade de letras minúsculas é superior a quantidade de caracteres disponíveis para a senha.')
else: 
    quantidade_letras_minusculas = 0

while True:
    se_caracteres_especiais = input('Terá Caracteres Especiais? [S/N] ').strip().upper()[0]
    if se_caracteres_especiais in 'SN':
        break
    print('Opção inválida.')
if se_caracteres_especiais == 'S':
    while True:
        quantidade_caracteres_especiais = int(input('Quantos caracteres especiais? '))
        if quantidade_caracteres_especiais <= limite:
            limite = limite - quantidade_caracteres_especiais
            break
        print('A quantidade de caracteres especiais é superior a quantidade de caracteres disponíveis para a senha.')
else: 
    quantidade_caracteres_especiais = 0

caracteres_aleatórios_restantes = limite

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

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

caracteres_aleatórios_restantes_lista = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
    '!', '@', '#', '$', '%',
    '&', '*', '-', '_',
    '+', '=', '?'
    ]

senha = ''

for valor in range(quantidade_numeros):
    senha += numeros[randint(0, len(numeros) - 1)]


for valor in range(quantidade_letras_maiusculas):
    senha += letras_maiusculas[randint(0, len(letras_maiusculas) - 1)]


for valor in range(quantidade_letras_minusculas):
    senha += letras_minusculas[randint(0, len(letras_minusculas) - 1)]


for valor in range(quantidade_caracteres_especiais):
    senha += caracteres_especiais[randint(0, len(caracteres_especiais) - 1)]

if caracteres_aleatórios_restantes > 0:
    for valor in range(caracteres_aleatórios_restantes, 0, -1):
        senha += caracteres_aleatórios_restantes_lista[randint(0, len(caracteres_aleatórios_restantes_lista) - 1)]


#Embaralhar senha

'''Embaralha os caracteres e junta tudo em uma nova string
A função random.sample() seleciona todos os caracteres da string de forma aleatória,
retornando-os como uma lista. Em seguida, o "".join() junta essa lista de volta em um único texto contínuo.'''

senha_embaralhada = "".join(random.sample(senha, len(senha)))

print(senha_embaralhada)