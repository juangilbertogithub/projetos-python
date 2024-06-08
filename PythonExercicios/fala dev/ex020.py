compra=float(input('Insira o valor da compra: \nR$'))
if compra < 20:
    print(f'Você obterá um lucro de 45% do valor vendendo por R${compra*1.45:.2f}')
else:
    print(f'Você obterá um lucro de 30% do valor vendendo por R${compra*1.3:.2f}')


#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00;
#caso contrário, o lucro será de 30%. Escreva um programa em Python que receba o valor do produto e exiba o valor da venda.