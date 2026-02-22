from datetime import date
atual = date.today().year
nasc = int(input("Em que ano o atleta nasceu? "))
clas = atual - nasc
print(f'Esse nadador tem {clas} anos.')
if clas  < 9 :
    print('Até 9 anos: MIRIM')
elif clas >= 9 and clas < 14:
    print('– Até 14 anos: INFANTIL')
elif clas >= 14 and clas < 19:
    print ('– Até 19 anos: JÚNIOR')
elif clas  >= 19 and clas <25 :
    print(' Até 25 anos: SÊNIOR')
else :
    print("– Acima de 25 anos: MASTER")

