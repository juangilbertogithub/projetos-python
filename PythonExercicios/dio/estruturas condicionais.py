maior_idade=18
idade_especial=17
idade=int(input('Digite sua idade: '))
if idade>=maior_idade:
    print('Maior de idade, pode tirar CNH.')
elif idade==idade_especial:
    print('Pode aulas teórias, mas não pode prática.')
else:
    print('Menor de idade, não pode tirar CNH.')


saldo=1
saque=1
status='Sucesso' if saldo>=saque else 'Falha'
print(f'{status} ao realizar o saque.')


a=int(input('Informe um número: ')) #sem repetiçao
print(a)
a+=1
print(a)
a+=1
print(a)

a=int(input('Informe um número: ')) #com repetiçao
print(a)
for c in range (0,2):
    a+=1
    print(a)

texto=input('Insira um texto: ')
VOGAIS='AEIOU'
for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end=' ')
    else:
        print('Fim da execução.')

range(4)
range(0,4)
list(range(0,10))
list(range(10))

for numero in range (0,11) # ou apenas (11) porque já reconhece normalmente que começa do zero
    print(numero, end=' ')

for numero in range (0,51,5):
    print(numero, end=' ')

for numero in range (100):
    if numero%2==0:
        continue
    print(numero, end=' ')

for numero in range (100):
    if numero==12:
        continue
    print(numero, end=' ')