km = float(input("Qual a distância em km da sua viagem?"))
passagem1 = km * 0.50 #ate 200km
passagem2 = km * 0.45 # >200km
if km <= 200 :
    print(f'O preço da sua viagem é de {passagem1}')

else:
    print(f'O valor da sua viagem é de {passagem2}')

