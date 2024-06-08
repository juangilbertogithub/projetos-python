preco=float(input('Insira o valor do produto: \nR$'))

print("""Condições de pagamento
1 - À vista em dinheiro ou débito, recebe 10% de desconto
2 - À vista no cartão de crédito, recebe 5% de desconto
3 - Em 2 vezes, preço normal de etiqueta sem juros
4 - Em 3 vezes, preço normal de etiqueta mais juros de 10%""")

pagamento=int(input('Escolha um pagamento: '))

if pagamento==1:
    print(f'O valor total a ser pago será de R${preco*0.9:.2f}')
elif pagamento==2:
    print(f'O valor total a ser pago será de R${preco*0.95:.2f}')
elif pagamento==3:
    print(f'O valor total a ser pago será 2X de R${preco/2:.2f}')
elif pagamento==4:
    print(f'O valor total a ser pago será 3X de R${(preco*1.1)/3:.2f}')
else:
    print('Valor inserido inválido')



#Elabore um programa que calcule e mostre o valor que deve ser pago por um produto, considerando que o usuário irá fornecer
#o preço normal de etiqueta e o código da  condição de pagamento.
#Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#Código
#Condições de pagamento
#1
#À vista em dinheiro ou débito, recebe 10% de desconto
#2
#À vista no cartão de crédito, recebe 5% de desconto
#3
#Em 2 vezes, preço normal de etiqueta sem juros
#4
#Em 3 vezes, preço normal de etiqueta mais juros de 10%