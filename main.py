# Dicionario com indiomas
cidades = {'Br': 'Portugues', 'Eua': 'Ingles', 'Esp': 'Espanhol', 'Argentina': 'Espanho_latin'}
# lista
cid = ['Br' 'Portugues', 'Eua''Ingles', 'Esp' 'Espanhol', 'Argentina' 'Espanho_latin']
# tupla
dados = ('Br' 'Portugues', 'Eua' 'Ingles', 'Esp' 'Espanhol', 'Argentina' 'Espanho_latin')

# print(type(cidades))
# print(dir(dados))
# for v, i, in enumerate(cidades.items()):
#   print(v, i, )

"""def somar(a: int, b: int) -> int: # Aqui estamos usando o type-hint 
    :param a: # Aqui será adcionado um número
    :param b: # aqui será adcionado o segundo número
    :return:  # Aqui será o resultado da soma entre a + b
    
    #caso queira usar o input elimine o uso do #return
    #return a + b
    #print(somar(77,85))"""

def somar() -> int:

    a = int(input('Digite um numero: '))
    b = int(input('Digite Outro Número: '))
    result = a + b
    print(result)
somar()
