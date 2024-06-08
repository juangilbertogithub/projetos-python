cont=soma=0
while True:
    n=int(input('Digite um número (999 para parar): '))
    if n==999:
        break
    else: #nem precisa desse else
        cont+=1
        soma+=n

print(f'Foram inseridos {cont} número e sua soma deu {soma}.')
