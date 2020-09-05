# Capturando as primeiras letras Maiusculas de um Nome

nome = str(input('Digite Um Nome: '))
l = []
for letras in nome:
    letra_maiucula = letras[0]
    if letra_maiucula.isupper():
        l.append(letra_maiucula)
print(l)
