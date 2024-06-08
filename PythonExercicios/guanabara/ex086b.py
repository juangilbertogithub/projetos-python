lista=list()
contagem=0

print(f'Matrix 3x3\nDigite um valor de até 5 casas.\n')

for c in range (1,10):
       lista.append(int(input(f'Posição {c} = ')))

"""for c,v in enumerate (lista):
       contagem+=1
       if contagem%3==0:
              print(f'{v}\n')
       else:
              print(v,end=' ')"""


print(f'[{lista[0]:^5}][{lista[1]:^5}][{lista[2]:^5}]')
print(f'[{lista[3]:^5}][{lista[4]:^5}][{lista[5]:^5}]')
print(f'[{lista[6]:^5}][{lista[7]:^5}][{lista[8]:^5}]')

#OU

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linha in range (0,3):
       for coluna in range(0,3):
              matriz[linha][coluna]=int(input(f'Digite um valor para [{linha},{coluna}]: '))

for linha in range (0,3):
       for coluna in range(0,3):
              print(f'[{matriz[linha][coluna]:^5}]',end='')
       print()