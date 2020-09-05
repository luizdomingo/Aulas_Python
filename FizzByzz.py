# ou se um numero for divisivel por 2 e por 5 então trazer como resultado 
# o nome fizzbuzz
# Ex: se for divisivel somente por 2 traga como resultado fizz
# se for divisivel por 5 traga somente buzz
# se for por 2 e 5 traga fizzbuzz

def FizzBuzz():
    try:
        numero = int(input('Digite um número para verificação: '))
        if numero % 3 == 0 and numero % 5 == 0:
            return f'Fizzbuzz, O número {numero} é divisivel por 3 e 5'
        elif numero % 3 == 0:
            return f'Fizz, O número {numero} é divisivel por 3 '
        elif numero % 5 == 0:
            return f'Buzz, O número {numero} é Divisivel por 5'
        return f'{numero} não é divisivel por 3 nem por 5'
    except:
        print('Digite apenas numero..')


print(FizzBuzz())
