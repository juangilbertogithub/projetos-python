"""n=int(input('Digite um intervalo que será seguido por 6 números: '))

s=0
for c in range (n,n+7):
    if c%2==0:
        s+=c

print(f'Seu somatório é de {s}')"""

soma=0
cont=0
for c in range (1,7):
    num= int(input(f'Digite o {c} valor: '))
    if num%2==0:
        soma = soma+num
        cont = cont+1
print(f'Você informou {cont} números PARES e a soma foi {soma}.')