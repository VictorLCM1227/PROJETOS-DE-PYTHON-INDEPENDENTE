from random import randint
from random import sample

print('=' * 50)
print(f'{" BEM-VINDO(A) AO GERADOR DE SENHAS DO VICTOR! ":^50}')
print('=' * 50)

limite = tamanho_da_senha = int(input('Tamanho da senha: '))
se_algo = {}
quantidade_algo = {}

def se(algo):
    global limite
    while True:
        se_algo[algo] = input(f'Terá {algo}? [S/N] ').strip().upper()[0]
        if se_algo[algo] in 'SN':
            break
        print('Opção inválida.')
    if se_algo[algo] == 'S':
        while True:
            quantidade_algo[algo] = int(input(f'Quanto(a)s {algo}? '))
            if quantidade_algo[algo] <= limite:
                limite = limite - quantidade_algo[algo]
                break
            print(f'A quantidade de {algo} é superior a quantidade de caracteres disponíveis para a senha.')
    else:
        quantidade_algo[algo] = 0

        
def gera_senha(algo):
    global senha
    for valor in range(quantidade_algo[algo]):
        senha += caracteres[algo][randint(0, len(caracteres[algo]) - 1)]



se('numeros')
se('letras_maiusculas')
se('letras_minusculas')
se('caracteres_especiais')

quantidade_algo['caracteres_aleatórios_restantes'] = limite

caracteres = {'letras_maiusculas': [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

'letras_minusculas': [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'],

'caracteres_especiais' : [
    '!', '@', '#', '$', '%',
    '&', '*', '-', '_',
    '+', '=', '?'],

'numeros' : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
}

caracteres['caracteres_aleatórios_restantes'] = caracteres['numeros'] + caracteres['letras_maiusculas'] + caracteres['letras_minusculas'] + caracteres['caracteres_especiais']

senha = ''

gera_senha('numeros')
gera_senha('letras_maiusculas')
gera_senha('letras_minusculas')
gera_senha('caracteres_especiais')

if limite > 0:
    gera_senha('caracteres_aleatórios_restantes')


#Embaralhar senha

'''Embaralha os caracteres e junta tudo em uma nova string
A função random.sample() seleciona todos os caracteres da string de forma aleatória,
retornando-os como uma lista. Em seguida, o "".join() junta essa lista de volta em um único texto contínuo.'''

senha_embaralhada = "".join(sample(senha, len(senha)))

print(senha_embaralhada)