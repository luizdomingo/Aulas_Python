# Crie uma função que receba 2 numeros  um é o valor o outro é o percentual
# Ex: 10% , retorne o valor do primeiro numero somado do almento do percentual do mesmo.

def almento_percentual() -> float:
    valor = float(input('Digite o valor do seu Salario: '))
    percentual = float(input('Digite o quantos porcento de almento você Quer: '))
    resultado = valor + (valor * percentual / 100)
    print(f'O Novo Valor será R${resultado:.2f}')

almento_percentual()
