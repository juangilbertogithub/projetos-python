from random import randint

lista = []


def maior(num):
    if num == 0:
        print('0 valores foram informados, logo, o maior será 0.')
    else:
        print(f'Foram informados {num} valores. Os valores da lista foram: ', end='')
        for c in range (num):
            numero=randint(1,10)
            lista.append(numero)
            print(numero, end=' ')
        print('.')
        print(f'O maior valor é o {max(lista)}')
        lista.clear()


maior(6)
maior(3)
maior(2)
maior(1)
maior(0)
