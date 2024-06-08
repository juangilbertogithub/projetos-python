salario=float(input('Insira o valor do salário mínimo: \nR$'))
agua=int(input('Insira o valor de água consumida no mês em litros: '))
valor=salario*0.02
conta=(agua/1000)*valor
print(f'Sua conta de água é de R${conta:.2f}')
print(f'Sua conta de água com o desconto de 15% é R${conta*0.85:.2f}')

#Sabe-se que o valor de cada 1000 litros de água corresponde a 2% do salário mínimo. Elabore um programa que receba o valor
#do salário mínimo e a quantidade de água consumida em uma residência por mês. Calcule e mostre:
#a) O valor da conta de água.
#b) O valor a ser pago com desconto de 15%.