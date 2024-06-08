escolha=True
contagem=0
soma=0

while escolha == True:
    numero=int(input('Digite um valor: '))
    contagem += 1
    soma+=numero

    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta=str(input('Deseja continuar? [S/N]: '))[0].strip().upper()

    if resposta == 'N':
        escolha=False

media = soma / contagem
print(f'A média dos valores inserido é {media}, o maior valor é {maior} e o menor valor é {menor}.')





