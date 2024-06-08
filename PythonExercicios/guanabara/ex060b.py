numero=int(input('Insira um valor para descobrir seu fatorial: '))
contagem=numero
total=numero
parar=False

while parar == False:
    total *= contagem #mesma coisa que total = total * contagem
    contagem-=1

    if contagem == 1:
        parar=True
        
print(f'O fatorial de {numero}! é {total}.')

"""print(f'O fatorial de {numero}! é ', end='')
while contagem > 0:
    total = total * contagem
    print(contagem, end='')
    print(' x ' if contagem>1 else ' = ', end='')
    contagem -=1
print(total)"""  #maneira mais confusa e complicada
