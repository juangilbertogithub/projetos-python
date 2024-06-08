def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: Mostra ou não a conta (opcional)
    :return: O valor do numero n
    """
    n = 1
    if show==True:
        for c in range(num, 0, -1):
            n *= c
            print(c, end=' ')
            if c!=1: #ou if c>1
                print('x', end=' ')
            else:
                print('=', end=' ')
        return n
    else:
        for c in range(num, 0, -1):
            n *= c
        return n

"""    f = 1 #n funciona
    for c in range (num,0,-1):
        if show==True:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*=c
    return f"""


num=int(input('Insira um valor: '))
print(fatorial(num,True))