num = int(input("Digite um numero inteiro : "))
print('''Bases para conversão:
 [1] converter para BINÁRIO
 [2] converter para OCTAL 
 [3] converter para HEXADECIMAL''')

escolha = int(input('Escolha a base desejada : '))

if escolha ==   1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:].upper()}')
else:
    print('Opção inválida ')