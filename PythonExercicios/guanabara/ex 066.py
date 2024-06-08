cont=0
soma=0

while True:
    n=int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
    
print(f'Foram digitados {cont} números. A soma entre os números é {soma}.')