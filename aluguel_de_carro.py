
dia = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos quilometros foram percorridos?'))
diaria  = (dia * 60)
kmr = (km * 0.15)
pg = (diaria + kmr)

print(f' O custo de diarias alugadas é de R${diaria:.2f},o custo de km rodados é de R${kmr:.2f}')
print(f'O valor total a ser pago é de R${pg:.2f}!')