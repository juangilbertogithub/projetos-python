import datetime
from time import sleep

print('-'*20)
print("Descubra a sua categoria")
print('-'*20)
print("""Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER""")
print('-'*20)

sleep (1)

idade=int(input('Digite seu ano de nascimento: '))
tempo=datetime.date.today().year

anos=tempo-idade

sleep(1)

"""if anos<=9:
    print('Você é um MIRIM')
if 9<anos<=14:
    print('Você é um INFANTIL')
if 14<anos and anos<=19:
    print('Você é um JUNIOR')
if 19<anos<=25:
    print('Você é um SÊNIOR')
if anos>25:
    print ('Você é um MASTER')"""

if anos<=9:
    print('Você é um MIRIM')
elif anos<=14:
    print('Você é um INFANTIL')
elif anos<=19:
    print('Você é um JUNIOR')
elif anos<=25:
    print('Você é um SÊNIOR')
else:
    print ('Você é um MASTER')