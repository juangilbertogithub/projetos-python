salario=float(input('Digite o seu salário: '))
if salario >= 1250:
    aumento= (salario * 10 / 100) + salario
    print(f'Parabéns! O seu salário subiu de R${salario:.2f} para R${aumento:.2f}!')
else:
    aumento = (salario * 15/100) +salario
    print(f'Parabéns! O seu salário subiu de R${salario} para R${aumento:.2f}!')