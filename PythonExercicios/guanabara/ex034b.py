salario=float(input('Digite o valor do seu salário: '))
if salario >1250:
    salarionovo=salario*0.1+salario
    print(f'Após um aumento de 10% seu salário passará a ser R${salarionovo:.2f}.')
if salario <=1250:
    salarionovo=salario*0.15+salario
    print(f'Após um aumento de 15% seu salário passará a ser R${salarionovo:.2f}.')