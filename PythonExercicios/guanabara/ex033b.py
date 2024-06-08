n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
"""lista=(n1,n2,n3)
print(max(lista))
print(min(lista))"""

maior=n1
menor=n1
if n2>n1:
    maior=n2
if n3>n2:
    maior=n3
if n3>n1:
    maior=n3
if n2<n1:
    menor=n2
if n3<n2:
    menor=n3
if n3<n1:
    menor=n3

print(maior)
print(menor)
