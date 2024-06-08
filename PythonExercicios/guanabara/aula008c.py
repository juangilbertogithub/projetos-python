'''import math
n=int(input('Digite um número: '))
raiz=math.sqrt(n)
print(f'A raíz de {n} é {raiz}')

#ou

from math import sqrt
raiz=sqrt(n)
print(f'A raíz de {n} é {raiz}.')'''

frase='Curso em Vídeo Python'
print(frase)
print(frase[3])
print (frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.find('o'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Curso')) #print(frase.find('vídeo')) vai mostrar -1 por não existir no texto (o python diferencia maiúsculo de minúsculo)
print(frase.split())

dividido=frase.split()
print(dividido[0])
print(dividido[2][3])