lista=('zero','um','dois','tres','quatro','cinco', 'seis','sete','oito','nove','dez','onze','doze','treze','catorze', 'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

"""n=int(input('Digite um valor entre 0 e 20: '))

while not 0 <= n <= 20:
    print('Esse valor não existe. Por favor, tente novamente')
    n = int(input('Digite um valor entre 0 e 20: '))

    print(f'Você digitou o número {lista[n]}.')"""

while True:
    while True:
        n=int(input('Digite um valor entre 0 e 20: '))
        if 0<=n<=20:
            break
        print('Tente novamente')
    print(lista[n])

    resp=str(input('Gostaria de continuar? [S/N]')).upper().strip()[0]
    if resp=='N':
        break

print('fim')