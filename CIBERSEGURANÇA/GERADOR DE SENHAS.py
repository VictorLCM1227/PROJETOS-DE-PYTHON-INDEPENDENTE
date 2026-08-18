from random import randint
from random import sample


# ==============================
# CONFIGURAÇÃO
# ==============================

caracteres = {
    'letras_maiusculas': [
        'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ],

    'letras_minusculas': [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z'
    ],

    'caracteres_especiais': [
        '!', '@', '#', '$', '%',
        '&', '*', '-', '_',
        '+', '=', '?'
    ],

    'numeros': [
        '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0'
    ]
}


quantidade_algo = {}


# ==============================
# INTERFACE
# ==============================

def cabecalho():
    print('=' * 50)
    print(f'{" BEM-VINDO(A) AO GERADOR DE SENHAS DO VICTOR! ":^50}')
    print('=' * 50)


# ==============================
# CONFIGURAÇÃO DA SENHA
# ==============================

def escolher_quantidade(algo, limite):
    while True:
        try:
            quantidade = int(
                input(f'Quanto(a)s {algo}? ')
            )

            if quantidade < 0:
                print('A quantidade não pode ser negativa.')
                continue

            if quantidade <= limite:
                quantidade_algo[algo] = quantidade
                return limite - quantidade

            print(
                f'A quantidade de {algo} é superior '
                f'à quantidade de caracteres disponíveis.'
            )

        except ValueError:
            print('Digite um número inteiro válido.')


def escolher_caracteres(algo, limite):
    while True:
        resposta = input(
            f'Terá {algo}? [S/N] '
        ).strip().upper()

        if not resposta:
            print('Digite S ou N.')
            continue

        if resposta[0] not in 'SN':
            print('Opção inválida.')
            continue

        if resposta[0] == 'S':
            return escolher_quantidade(algo, limite)

        quantidade_algo[algo] = 0
        return limite


# ==============================
# GERAÇÃO
# ==============================

def gera_senha(algo, senha):
    for valor in range(quantidade_algo[algo]):
        indice = randint(
            0,
            len(caracteres[algo]) - 1
        )

        senha += caracteres[algo][indice]

    return senha


def embaralhar_senha(senha):
    return ''.join(sample(senha, len(senha)))


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

cabecalho()

tamanho_da_senha = int(
    input('Tamanho da senha: ')
)

limite = tamanho_da_senha

for tipo in caracteres:
    limite = escolher_caracteres(tipo, limite)

# Caracteres que podem preencher
# o restante da senha
caracteres['caracteres_aleatórios_restantes'] = (
    caracteres['numeros']
    + caracteres['letras_maiusculas']
    + caracteres['letras_minusculas']
    + caracteres['caracteres_especiais']
)

quantidade_algo['caracteres_aleatórios_restantes'] = limite

senha = ''

for tipo in caracteres:
    senha = gera_senha(tipo, senha)

senha = embaralhar_senha(senha)

print()
print(f'Senha gerada: {senha}')