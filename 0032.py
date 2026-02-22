from datetime import date
ano = int(input('Qual ano você quer analizar? Coloque 0 para analizar o ano atual.'))
if ano == 0 :
    ano = date.today().year # pega o ano da máquina

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0 : #não entendi bem essas condições, preciso estudar mais matematica

    print(f'{ano} é um ano BISSEXTO')

else:
    print(f'{ano} NÃO é um ano bissexto!')