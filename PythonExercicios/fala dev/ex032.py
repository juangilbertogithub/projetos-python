soma=0
numero=int(input('Insira um número inteiro e positivo: '))
while numero<=0:
    print('Valor inválido! O número deve ser inteiro e positivo.')
    numero = int(input('Insira um número: '))
print('H = ',end='')
for c in range(1,numero+1):
    soma += 1 / c
    if c==1:
        print('1',end=' + ')
    else:
        print(f'1/{c}',end='')
        if c < numero:
            print(' + ',end='')
        if c == numero:
            print(' = ',end='')
            print(soma)


#Leia um número n, inteiro e positivo, calcule e apresente: 𝐻 = 1 + 1/ 2 + 1/3 + 1/4 + ⋯ + 1/𝑛