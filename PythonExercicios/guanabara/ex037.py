num=int(input('Digite um número inteiro: '))
print('''Digite uma base de conversão:
1- Binário
2- Octal
3- Hexadecimal''')
opçao=int(input('Opção: '))

if opçao==1:
    print(f'O valor {num} em binário é {bin(num)[2:]}.')
elif opçao==2:
    print(f'O valor {num} em octal é {oct(num)[2:]}.')
elif opçao==3:
    print(f'O valor {num} em hexadecimal é {hex(num)[2:]}.')
else:
    print('Opção inválida. Por favor, digite novamente.')