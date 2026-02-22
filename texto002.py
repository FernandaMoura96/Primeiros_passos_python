#Aprenderemos como dividir str e int
num = int(input ("Digite um numero de ate 4 digitos: "))
#todos os numeros serão dividos pelos seus semelhantes e depois 'pegar o resto(%)' de 10 veja exemplo
u = (num // 1 % 10)
d = (num // 10 % 10)
c = (num // 100 % 10)
m = (num // 1000 % 10)
print(f" {num} Tem : \n {u} unidades, \n {d} Dezenas \n {c} centenas \n {m} unidades de milhar.  ")