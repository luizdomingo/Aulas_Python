import unittest
# criando um programa onde se o rsto de uma divisão for igual a 0
# ou se um numero for divisivel por 2 e por 5 então trazer como resultado 
# o nome fizzbuzz
# Ex: se for divisivel somente por 2 traga como resultado fizz
# se for divisivel por 5 traga somente buzz
# se for por 2 e 5 traga fizzbuzz


def fizz_buzz(n: int):
    resultado = []
    for numero in range(1, n + 1):
        fizalgarismo = ''
        if numero % 2 == 0:
            fizalgarismo ='fizz'
        elif numero % 5 == 0:
            fizalgarismo ='buzz'
        if fizalgarismo == '':
            fizalgarismo = str(numero)
        resultado.append(fizalgarismo)
    return resultado
    

class TesteFizzBuzz(unittest.TestCase):
    def test_com_10(self):
        entrada = 10
        resultado = fizz_buzz(entrada)
        resultado_eperado = [
            '1',
            'fizz',
            '3',
            'fizz',
            'buzz',
            'fizz',
            '7',
            'fizz',
            '9',
            'fizzbuzz'
        ]