import math
an = float(input('Digite o angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O angulo de {an} tem o seno de {sen:.4f}')
print(f'E o casseno de {cos:.4f}')
print(f'A tangente é de {tan:.4f}')
#quando especificamos as funções da biblioteca podemos
#eliminar os .math pois não é mais necessário referenciar
#Linguagem,Biblioteca/Objeto,Função Principal
#Python,import random,"random.random() ou random.randint(a, b)"
