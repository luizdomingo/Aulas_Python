# Conhecida como fucçoes anonimas, as lambddas , são funçoes que nao 
# precisamos usar o return, torna-se anonimas porque não precisa de um nome para 
# seu uso como uma função.

soma = lambda a, b: a + b
multiplicar = lambda a, b: a * b

subtracao = lambda y, function: y + function(y)
resposta = subtracao(1525, lambda y: y - 589)

print(resposta)
print(multiplicar(185, 289))
