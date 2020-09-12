# Capturando as primeiras letras Maiusculas de um Nome

nome = str(input('Digite Um Nome: '))
l = []
for letras in nome:
    letra_maiuscula = letras[0]
    if letra_maiuscula.isupper():
        l.append(letra_maiuscula)
cont = len(l)    
print(l)
print(cont)
