a=int(input('Escolha o primeiro termo: '))
r=int(input('Escolha uma razão: '))
n=a #n = a + (10) * r quando usava o for. tive q dar um novo termo pq se n ele n iria funcionar por pensar q iria inserir um novo valor?
c=1

while c<=10:
    print(f'{n}', end=' > ')
    c += 1
    n += r

print('FIM')