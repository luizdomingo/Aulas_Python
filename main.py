# Dicionario com indiomas
cidades = {'Br': 'Portugues', 'Eua': 'Ingles', 'Esp': 'Espanhol', 'Argentina': 'Espanho_latin'}
# lista
cid = ['Br' 'Portugues', 'Eua''Ingles', 'Esp' 'Espanhol', 'Argentina' 'Espanho_latin']
# tupla
dados = ('Br' 'Portugues', 'Eua' 'Ingles', 'Esp' 'Espanhol', 'Argentina' 'Espanho_latin')
from Exercicios.Ex01 import contar_caracteres
# print(type(cidades))
# print(dir(dados))
# for v, i, in enumerate(cidades.items()):
#   print(v, i, )


def somar(a, b):
    """
    :param a: # Aqui será adcionado um número
    :param b: # aqui será adcionado o segundo número
    :return:  # Aqui será o resultado da soma entre a + b
    """
    return a + b

if __name__ == '__main__':
    #print(somar(55, 125))
    print(contar_caracteres('Lais Clarice Misael domingo '))
