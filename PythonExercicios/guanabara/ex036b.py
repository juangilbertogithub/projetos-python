salario=float(input('Insira seu salário: '))

valor=float(input('Digite o valor da casa: '))
anos=int(input('Insira a quantidade de anos que irá pagar a casa: '))

mensalidade=anos*12
prestaçao=valor/mensalidade

if prestaçao > salario*0.3:
    print(f'Não será possível fazer o empréstimo. O valor da mensalidade (R${prestaçao:.2f}) é maior que 30% do seu salário (equivalente a R${salario*0.3:.2f}).')
else:
    print(f'Seu empréstimo foi aceito. Você deverá pagar uma parcela de R${prestaçao:.2f} mensais. O valor da mensalidade é maior que 30% do seu salário (equivalente a R${salario*0.3:.2f}).')