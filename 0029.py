km = float(input('Qual a velocidade do carro?'))
multa = (km - 60)*7

if km <= 60:
    print('parabens,você está dirigindo com cautela')

else:
    print(f'Você ultrapassou o limte de 60 km/h, \n deve pagar o valor de {multa} como multa por exesso de velocidade')
