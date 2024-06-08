def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print('erro')
        return False
print(divide(2,0))

def divide(n1,n2):
    if n2==0:
        raise ValueError('N2 não pode ser 0.')
    return n1/n2
print(divide(2,0))