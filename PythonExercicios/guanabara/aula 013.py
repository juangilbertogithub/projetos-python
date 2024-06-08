for c in range (1,6):
    print('C')
print('FIM')

for c in range (0,6):
    print('Oi')
print('FIM')

for c in range (6,0,-1): #o -1 é pra contar ao contrario
    print('Oi')
print('FIM')

for c in range (0,6,2): #foi até o ultimo numero pulando de 2 em 2
    print('Oi')
print('FIM')

n=int(input('Digite um número: '))
for c in range (0,n+1):
    print(c)
print('FIM')

i=int(input('INÍCIO: '))
f=int(input('FIM: '))
p=int(input('PASSO: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')

for c in range (0,3):
    n=int(input('Digite um valor: '))
print('FIM')

s=0
for c in range (0,4): #somatorio
    n=int(input('Digite um valor: '))
    s+=n
print(f'O somatório de todos os valores foi {s}.')