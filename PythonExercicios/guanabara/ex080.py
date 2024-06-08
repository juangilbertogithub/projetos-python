lista=[]
menor=maior=0

print('Insira um valor numérico: ')
for c in range (0,5):
    v=int(input(f'{c+1}º valor: '))

    if c==0 or v>lista[-1]: #se for o primeiro ou maior que o ultimo
        lista.append(v)

    else:
        pos=0
        while pos < len(lista): #vai de pos até a ultima posiçao
            if v <= lista[pos] #verificar se o numero é menor ou igual a ele. se for, vai inserir em um lugar especifico
                lista.insert(pos,v)
                break
            pos+=1

print(f'Lista dos números em ordem: {lista}')