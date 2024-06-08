numero=int(input('Digite um número de 3 dígitos: '))
dezena=(numero%100)//10
if dezena%2==0:
    print(f'O algarismo do {numero} é {dezena}. É par.')
else:
    print(f'O algarismo do {numero} é {dezena}. É ímpar.')

#Escreva um programa que leia um número inteiro de 3 dígitos e imprima se o algarismo da dezena é par ou ímpar.