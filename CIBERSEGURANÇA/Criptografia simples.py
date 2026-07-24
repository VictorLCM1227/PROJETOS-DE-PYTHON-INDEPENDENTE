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


def linha(tam = 42):
    return '-' * tam 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 0
    for item in lista:
        print(f'\033[33m[{contador}]\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

def criptografar(msg_texto, msg_chave):
    texto = input(msg_texto)
    chave = leiaInt(msg_chave)
    texto_numeros = []
    texto_senha = []
    for letra in texto:
        texto_numeros.append(ord(letra) + chave)
    for numero in texto_numeros:
        texto_senha.append(chr(numero))
    criptografado = "".join(texto_senha)
    return criptografado

def descriptografar(msg_texto, msg_chave):
    criptografado =input(msg_texto)
    chave = leiaInt(msg_chave)
    texto_numeros = []
    texto_senha = []
    for letra in criptografado:
        texto_numeros.append(ord(letra) - chave)
    for numero in texto_numeros:
        texto_senha.append(chr(numero))
    descriptografado = "".join(texto_senha)
    return descriptografado




while True:
    resposta_menu = menu(['Sair', 'Criptografar', 'Descriptografar'])
    if resposta_menu == 0:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    elif resposta_menu == 1:
        cabeçalho('Criptografar')
        criptografado = criptografar(msg_texto='Digite a mensagem a ser criptografada: ', msg_chave='Chave da criptografia: ')
        print(criptografado)
    elif resposta_menu == 2:
        cabeçalho('Descriptografar')
        descriptografado = descriptografar(msg_texto='Digite a mensagem a ser descriptografada: ', msg_chave='Chave da criptografia: ')
        print(descriptografado)