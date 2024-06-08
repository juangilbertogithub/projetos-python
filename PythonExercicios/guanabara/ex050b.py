soma=0
cont=0
lista=[]
for c in range (1,7):
    numero=int(input('Digite um número: '))
    lista=lista+[numero]
    if numero%2==0:
        soma+=numero
        cont+=1
print(f'Os números inseridos foram: {lista}. Foram somados {cont} números pares. Deu {soma}.')