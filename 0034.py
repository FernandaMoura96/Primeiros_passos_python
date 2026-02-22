salario = float(input("Qual é o salário do funcionário?  "))
if salario >= 1250.00:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f"O valor do novo salário é de {aumento :.2f}")
