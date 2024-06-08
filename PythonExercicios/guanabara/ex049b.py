print('-='*10)
print(f'{"TABUADA":^20}')
print('-='*10)

numero=int(input('Digite o valor desejado: '))
print(f'Tabuada de {numero}')
for c in range (0,11):
    print(f'{numero} x {c} = {numero*c}')