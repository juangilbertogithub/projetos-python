lista=list()
soma_pares=0
soma_terceira_coluna=0
maior_segunda_linha=list()

print(f'Matrix 3x3\nDigite um valor de até 5 casas.\n')

for c in range (1,10):

    numero=int(input(f'Posição {c} = '))
    lista.append(numero)

    if c==4 or c==5 or c==6:
        maior_segunda_linha.append(numero)
    if numero%2==0:
        soma_pares+=numero
    if c==3 or c==6 or c==9:
        soma_terceira_coluna+=numero

print(f'[{lista[0]:^5}][{lista[1]:^5}][{lista[2]:^5}]')
print(f'[{lista[3]:^5}][{lista[4]:^5}][{lista[5]:^5}]')
print(f'[{lista[6]:^5}][{lista[7]:^5}][{lista[8]:^5}]')

print(f'A soma de todos os números pares é: {soma_pares}.')
print(f'A soma da terceira coluna é: {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é: {max(maior_segunda_linha)}.')

#OU

matriz=[[0,0,0],[0,0,0],[0,0,0]] #foi uma maneira diferente de fazer e q n esperava. acho o meu mais claro
soma_paresb=som_colunab=0
for linha in range (0,3):
       for coluna in range(0,3):
              matriz[linha][coluna]=int(input(f'Digite um valor para [{linha},{coluna}]: '))

for linha in range (0,3):
       for coluna in range(0,3):
              print(f'[{matriz[linha][coluna]:^5}]',end='')
              if matriz[linha][coluna]%2==0:
                  soma_paresb+=matriz[linha][coluna]
       print()

for linha in range(0,3):
    som_colunab+=matriz[linha][2]

print(f'A soma de todos os pares é: {soma_paresb}')
print(f'A soma dos valores da terceira coluna é: {som_colunab}')
print(f'O maior da segunda coluna é: {max(matriz[1])}')