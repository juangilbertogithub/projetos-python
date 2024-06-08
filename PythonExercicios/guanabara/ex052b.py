n=int(input('Digite um número: '))
total=0
for c in range (1,n+1):
    if n%c==0:
        total+=1
        print(f'{c}',end=' ')
print()
if total>2:
    print(f'Possui um total de {total} números primos.')
else:
    print(f'Não é primo')