import math
co = float(input('Quanto mede o cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
hi = math.hypot(ca, co)
print(f'A hipotenusa mede {hi:.2f}')
