from time import sleep #sei la, exercicio estranho

def contador(inicio,fim,passo):      #pra contar de 5 a -5 o tutorial fez de outra forma
    print(f'Contando de {inicio} a {fim} em {passo} passos.')
    if passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.25)
        print()
    if passo < 0:
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.25)
        print()

inicio=int(input('Insira o valor inicial: '))
fim=int(input('Insira o valor final: '))
passo=int(input('Insira o passo: '))

contador(1,10,1)
contador(10,0,-2)

print('Contagem personalizada: ')
contador(inicio,fim,passo)