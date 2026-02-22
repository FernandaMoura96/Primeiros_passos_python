valor = float(input('Qual o valor do produto?'))

perc = valor - (valor*5/100)
print(f' O produto com 5% de desconto custará R${perc:.2f}')