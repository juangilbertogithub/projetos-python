from time import sleep

print('-'*25)
print('Calculadora de prestações')
print('-'*25)

sleep(0.5)

casa=float(input('Insira o valor da casa:\n R$'))
salario=float(input('Insira o seu salário:\n R$'))
anos=int(input('Insira em quantos anos irá pagar: '))

prestaçao=casa/(anos*12)
exceder=(salario*30/100)

print("\nCalculando...\n")

sleep(2)

if prestaçao>exceder: #if prestacao > (salario * 0.3):
    print(f'Desculpe. Não será possível efetuar esta compra. A prestação de R${prestaçao:.2f} excede 30% do seu salário de R${salario:.2f}.')
else: #if prestaçao<=exceder:
    print(f'Parabéns! Você poderá efetuar essa compra. A prestação de R${prestaçao:.2f} não excede 30% do seu salário de R${salario:.2f}.')

print('-'*25)
