valor=int(input('Digite quantas maçãs gostaria de comprar: '))

if valor < 12:
    preço=1.3
if valor >= 12:
    preço=1

preco_final=valor*preço

print(f'O valor final a ser pago é de R${preco_final:.2f}')

#outra maneira

quantidade=int(input('Digite quantas maçãs gostaria de comprar: '))
if quantidade <12:
    print(f'O valor final a ser pago é de R${quantidade*1.3:.2f}')
else:
    print(f'O valor final a ser pago é de R${quantidade:.2f}')





#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva
#um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.