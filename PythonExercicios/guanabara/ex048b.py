s=0
print('Somando os números ímpares múltiplos de 3')

for c in range (1,501):
    if c%3==0 and c%2!=0:
        s+=c

"""for c in range (1,501,2):
    if c%3==0:
        s+=c"""

print(f'A soma {s}')