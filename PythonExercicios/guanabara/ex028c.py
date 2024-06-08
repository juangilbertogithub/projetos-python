import random
import time
valor=random.randint(0,5)

numero = int(input('Insira um número entre 0 e 5: '))

print('Processando...')
time.sleep(1.5)

if numero == valor:
    print(f'Você acertou! O valor é {valor}.')

else:
    print(f'Você errou. O valor é {valor}, mas você escolheu {numero}.')
