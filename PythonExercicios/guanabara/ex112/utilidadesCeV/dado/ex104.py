"""def leiaInt(n): #exercicio esquisito
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('Erro! O valor inserido não é um número.')


n=leiaint('Digite um n: ')
print(f'Você digitou o número {n}')"""

def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('Erro! Esse valor não é um número.')
        if ok:
            break

n=leiaint('Insira um valor n: ')
print(f'Você digitou o número {n}')
