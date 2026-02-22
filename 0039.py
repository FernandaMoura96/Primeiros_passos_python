from datetime import date
atual = date.today().year
nasc = int(input( 'Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc}, tem {idade} em {atual}')
if idade == 18 :
    print("Você tem que se alistar IMEDIATAMENTE")
elif idade <18 :
    saldo = 18 - idade
    print(f'Você deverá se alistar em  {saldo} anos.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado a {saldo} anos.')