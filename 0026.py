frase = str(input("Digite uma frase: ")).strip().upper()
print(f"Sua frase tem {frase.count("A")} letras 'A' ")
print(f"A pimeira leta A aparece na posição {frase.find("A")+1}")
print(f"A ultima vez que a letra A aparece na frase é na posição {frase.rfind("A")+1}")