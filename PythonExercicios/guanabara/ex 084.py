lista=[]
dados=[]
menor=maior=0

print('Insira seu nome e peso')

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    lista.append(dados[:]) #copiano os dados q acabei de receber pra uma lista definitiva

    if len(lista) == 0:
        menor = maior = dados[1] #vou utilizar o dados q acabei de descobrir primeiro pra fazer esse tipo de coisa
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados [1] < menor:
            menor = dados[1]

    dados.clear() #apagando dados coletados para criar qnd for inserir novos

    resp=str(input('Deseja continuar? [S/N]: ').capitalize())[0]
    if resp == 'N':
        break

print(f'Foram registradas {len(lista)} pessoas.')


print(f'Maior peso: {maior}')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]}')

print(f'Menor peso: {menor}')
for c in lista:
    if c[1] == menor:
        print(f'{c[0]}')