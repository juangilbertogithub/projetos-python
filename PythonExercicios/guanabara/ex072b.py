lista=('Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
       'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
       'Vinte')

numero=int(input('Insira um número entre 0 e 20: '))
while True:
    if numero >20 or numero < 0:
        numero=int(input('Valor inválido. Insira um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {lista[numero - 1]}.')
        break
