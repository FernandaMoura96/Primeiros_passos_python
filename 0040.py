nota1 = float(input('Insira a primeira nota:'))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print(f'A média das notas é de {media:.2f}')
if media >= 7 :
    print('Parabéns você foi aprovado(a)!!!')
elif media < 7 and media > 5 :
    falta = 7 - media
    print(f'Você esta de recuperação e precisa de {falta:.2f} pontos para ser aprovado.  ')
elif media <= 5 :
    print('Lamento, você foi reprovado ')