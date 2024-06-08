import random #ou from random impor randint e por apenas o randint

lista=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))

print('Os números sorteados foram:')
#ou print(lista)
for l in lista:
    print(f'{l}', end=' ')

print(f'\nO valor máximo foi {max(lista)}.')
print(f'O valor menor foi {min(lista)}')