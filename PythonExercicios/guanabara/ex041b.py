import datetime
tempo=datetime.date.today().year

idade=int(input('Digite a sua idade: '))
#como analisa em ordem, n preciso colocar q é maior ou menor
if idade<= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
