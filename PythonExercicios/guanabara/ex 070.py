total=0
mais1000=0

menor=0
barato=''
cont=0

while True:
    produto=str(input('Digite o nome do produto: ')).strip()
    preço=int(input('''Digite o preço
R$: '''))

    cont+=1
    total += preço

    if preço >=1000:
        mais1000+=1

    if cont == 1 or preço< menor:
        menor=preço
        barato = produto

    continuar=str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(total,mais1000,barato)