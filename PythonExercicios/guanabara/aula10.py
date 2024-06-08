"""tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')"""

"""tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo<=3 else 'carro velho')
print('FIM')"""

"""nome=str(input('Qual é o seu nome? '))
if nome == 'Juan':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal...')
    print(f'Olá, {nome}.')"""

"""n1=float(input('Insira a sua primeira nota: '))
n2=float(input('Insira a sua segunda nota: '))
m= (n1+n2)/2
print(f'Sua média é de {m:.1f} pontos.')
if m >=6:
    print('Parabéns, você está aprovado!')
else:
    print('Você está reprovado.')"""

"""lista=[0,1,2,3,4,5]
import random
aleatorio=str(random.choice(lista))
n=int(input('Escolha um número de 0 a 5: '))
nint=str(n)
if aleatorio in nint:
    print(f'Você acertou! O número é {aleatorio}.')
else:
    print(f'Que pena, você errou. O correto era {aleatorio}.')"""
"""import random
n= int(input('Escolha um número entre 0 e 5: '))
x = random.randint(0,5)
if n == x:
    print('Você acertou!')
else:
    print(f'Você errou! O número era {x}')"""

"""carro=float(input('Está andando há quantos quilômetros? '))
if carro <=80:
    print('Nada acontece feijoada')
else:
    multa=(carro-80)*7
    print(f'Você ultrapassou os 80km/h! Sua multa será de R${multa:.2f}')"""

"""n=int(input('Digite um número: '))
if n%2==0:
    print('Seu número é par!')
else:
    print('Seu número é ímpar!')"""

"""km=float(input('Quantos quilômetro foram percorridos? '))
if km<=200:
    passagem=(km*0.5)
    print(f'Sua passagem custa R${passagem:.2f}.')
else:
    passagem=(km*0.45)
    print(f'Sua passagem custa R${passagem:.2f}.')"""

"""n=int(input('Digite o ano: '))
if n%4==0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')"""
"""n=int(input('Digite o ano: '))
if calendar.isleap(n) == True:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')"""

"""n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))
n3=float(input('Digite o terceiro valor: '))
lista=[n1,n2,n3]
print(f'O maior valor é {max(lista)}.')
print(f'O menor valor é {min(lista)}.')""""

"""salario=float(input('Digite o seu salário: \nR$'))
if salario >=1250:
    aumento=(salario*10/100)+salario
    print(f'Você obteve um aumento de 10% no seu salário! Você irá receber R${aumento:.2f} ao invés de R${salario:.2f}.')
else:
    aumento=(salario*15/100)+salario
    print(f'Você obteve um aumento de 15% no seu salário! Você irá receber R${aumento:.2f} ao invés de R${salario:.2f}.')"""

"""a=float(input('Digite o primeiro lado: '))
b=float(input('Digite o segundo lado: '))
c=float(input('Digite o terceiro lado: '))
if b-c<a<b+c:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')"""