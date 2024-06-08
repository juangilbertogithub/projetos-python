#fibonacci somo os dois termos anteriores

print('Sequência de Fibonacci')

n=int(input('Quantos termos gostaria de ver? '))
t1=0
t2=1
cont=3 #ja começa a partir do terceiro termo, pq o primeiro e segundo eu ja tenho

print(f'{t1} > {t2} > ', end='')
while cont<=n:
    cont+=1
    t3=t1+t2
    print(f'{t3}', end=' > ')
    t1=t2
    t2=t3

print('FIM')


"""print('Sequência de Fibonacci')
n=int(input('Digite quantos termos gostaria de ver: '))

t1=0
t2=1
cont=3

print(f'{t1} > {t2} > ', end='')
while cont<=n:
    t3=t1+t2
    cont += 1
    print(f'{t3}', end=' > ')
    t1=t2 #estou passando o numero pra frente pra ele somar.
    t2=t3

print('Fim')"""

