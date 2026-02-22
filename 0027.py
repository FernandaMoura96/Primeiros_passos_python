nome = str(input("Digite seu nome completo: ")).lower().strip()
posi = nome.split()
print(f'Seu primeiro nome é {posi [0].capitalize()}')

print(f"O seu ultimo nome é {posi[-1].capitalize()}")