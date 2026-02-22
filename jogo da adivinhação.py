from random import randint
pc = randint (0, 5)
print('=-=' *20)
print('Vou pensar em um número entre 0 e 5, e você deve tentar adivinhar')
print('=-=' *20)
gamer = int(input("Em qual número eu pensei?  "))
if gamer == pc:
    print(f"Parabéns, você venceu!!! Eu tinha pensado em {pc}")
else:
    print(f'Você perdeu! Eu pensei em {pc}')
