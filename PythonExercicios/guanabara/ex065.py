cont=0
soma=0
resposta=''

while resposta != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont==1:
        maior=num
        menor=num
    else:
        if num>maior:
            maior = num
        if num<menor:
            menor = num

media=soma/cont
print(f' A média é de {media:.1f}, o maior número é {maior} e o menor número é {menor}.')
