print('Olá, mundo')
print(7+4)
print('7'+'4') #eu posso juntar coisas diferentes dessa forma

#variaveis (recomendado escrever sempre com letra minuscula)
"""nome='Juan'
idade='25'
peso='60.5'

print(nome,idade,peso)
print(f'Meu nome é {nome}, tenho {idade} anos e peso {peso}kg.')"""

nome=str(input('Qual o seu nome? '))
idade=int(input('Qual a sua idade? '))
peso=float(input('Quanto você pesa? '))

print(f'Seu nome é {nome}, tem {idade} anos e pesa {peso}kg.')

dia=int(input('Que dia é hoje?'))
mes=str(input('Que mês estamos?'))
ano=int(input('Qual o ano?'))

print(f'Hoje é {dia} de {mes} de {ano}.')

n1=int(input('Insira um número: '))
n2=int(input('Insira outro número'))
#print(n1+n2) ou s=n1+n2 ; print(s) ou print=('A soma vale',s)
