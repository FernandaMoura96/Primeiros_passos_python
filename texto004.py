cid = str(input("Digite em que cidade você nasceu: ")).title().strip()
print(f"Analizando se inicia com Santo {cid}...")
ok = (cid[:5].title() == "Santo")
if ok == True:
    print("Sim,inicia com Santo")
else:
    print("Infelizmente não inicia com Santo")
#Aqui usei [:] para dividir a str e delimitar a pesquisa: