print("Vamos analizar sua proposta de emprestimo; ")

imovel = float(input("Qual o valor do imóvel em questão?  "))
tempo = int(input('Em quantos anos você pretende pagar o imóvel ? '))
entrada = float(input('Existe algum valor de entrada ? '))
renda = float(input('Qual a sua renda mensal? '))

meses = tempo * 12
financiamento = imovel - entrada
parcela = financiamento / meses
criterio =  renda  * 0.30


if criterio >= parcela:
    print(f'Você pode financiar este imóvel, o valor da sua parcela será de {parcela:.f}')
else:
    print("Infelizmente sua renda mensal não é suficianet para adquirir este imóvel, \n "
          "tente um valor maior de entrada, ou um imóvel de menor valor")
