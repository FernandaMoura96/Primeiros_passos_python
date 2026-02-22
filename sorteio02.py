import random

a = (input('Primeiro aluno: '))
b = (input('Segundo aluno: '))
c = (input('Terceiro aluno: '))
d = (input('Quarto aluno: '))
alunos = [a,b,c,d]
ordem = random.shuffle(alunos)

print(f'A ordem de apresentação dos alunos é: {alunos}')
