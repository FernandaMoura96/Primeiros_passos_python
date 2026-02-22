cid = str(input("Digite o nome de uma cidade: ")).title().strip()
print(f"Analizando {cid}....")
sto = "Santo"
a = cid.find(sto)
if a == (-1):
    print(f'A cidade não tem {sto} no nome ')
else:
    print('A cidade tem Santo no nome')
#fiz sozinha <3