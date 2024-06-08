km=float(input('Digite a quantidade de Km rodados: '))

if km <= 200:
    rodado=km*0.50
    print(f'O valor total a ser pago é de R${rodado:.2f}.')
if km >200:
    rodado=km*0.45
    print(f'O valor total a ser pago é de R${rodado:.2f}.')