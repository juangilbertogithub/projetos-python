#sexo=str(input('Insira seu sexo [M/F]: ')).upper().strip()[0]
sexo=str(input('Insira seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo=str(input('Erro. Insira novamente seu sexo [M/F]: ')).upper().strip()[0]
    """if opçao == 'M' and 'F':
        sexo=0
    if opçao != 'M' and 'F':
        sexo='x'
        print('Incorreto. Reinsira um valor válido.')"""

print('Fim')

#exercicio estranho. dificil de entender como funciona? prestar atençao da interaçao do while, como por exemplo, while not... OU while x not in...