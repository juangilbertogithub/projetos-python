n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
"""lista=[n1,n2,n3]
print(f'O maior valor é {max(lista)}.')
print(f'O menor valor é {min(lista)}.')"""
# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor é {menor}.')
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n2 > n3:
    maior = n3
print(f'O maior valor é {maior}.')
