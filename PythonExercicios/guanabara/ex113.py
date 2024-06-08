def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except:
            print('Valor inválido')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except:
            print('Valor inválido')
            continue
        else:
            return n

inteiro=leiaInt('Insira um valor inteiro: ')
real=leiaFloat('Insira um valor real: ')
print(f'Você digitou o número inteiro é {inteiro} e o número real é {real}.')