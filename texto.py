frase = str("Curso em video Python")
print(len(frase))
print(frase.find('f')) #devolve -1 else false
print(frase.count('o',0,13)) #conta quantas vezes tem a str desejada
print(frase.replace('Python','Android'))
print(frase.upper())#tudo maisculo
print(frase.lower())#tudo em minusculo
print(frase.capitalize())# primeira maiuscula,restante minuscula
print(frase.title()) #primeira letra de cada palavra maiuscula
#frase.strip() remove os espaços antes e depois da str
#frase.rstrip() remove espaços da direita
#frase.split() divide a str em varias str menores
print('Faça'.join(frase))