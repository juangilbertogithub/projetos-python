lista=[]
preço=contprod100=preçototal=contagem=menor=0
barato=' '
while True:

    produto=str(input('Insira o nome do produto: ')).strip().capitalize()

    lista += [produto]

    preço=int(input('Insira o valor do produto: '))
    contagem += 1
    preçototal += preço

    if preço >1000:
        contprod100+=1



    if contagem == 1 or preço<menor: #me enrolei nessa parte
        menor = preço
        barato=produto
    """else:
        if preço<menor:
            menor=preço
            barato=produto""" #desnecessario por causa do or em cima


    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Deseja continuar? ')).strip().upper()[0]
    if resposta=='N':
        break





print(f'Os produtos comprados foram: {lista}.')

print(f'O produto mais barato foi o {barato} que custou R${menor:.2f}.')

print(f'O total gasto foi de R${preçototal:.2f}')

if contprod100==0:
    print('Nenhum produto custou mais de R$1000.')
elif contprod100==1:
    print('1 produto custou mais de R$1000.')
else:
    print(f'{contprod100} produtos custaram mais de R$1000.')
