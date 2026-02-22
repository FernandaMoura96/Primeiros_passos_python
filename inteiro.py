import math

num = float(input('Digite um numero real: '))
parabaixo = math.floor(num)
paracima = math.ceil(num)
print(f'Arredondando o valor de {num} para cima é {paracima} \n e arredondando o valor baixo é {parabaixo}')

#Também podemos usar a função trunc :
# math.trunc(x)Retorna a parte inteira de $x$, removendo a parte fracionária
# (arredonda em direção a zero).
