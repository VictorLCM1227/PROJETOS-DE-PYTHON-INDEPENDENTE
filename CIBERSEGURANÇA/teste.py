texto = 'uva'
texto_numeros = []
texto_senha = []
for letra in texto:
    print(letra)
    texto_numeros.append(ord(letra)  + 1)
    print(texto_numeros)

for numero in texto_numeros:
    texto_senha.append(chr(numero))
    print(texto_senha)

senha = "".join(texto_senha)
print(senha)