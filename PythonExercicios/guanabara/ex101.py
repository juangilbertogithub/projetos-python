def voto(num):
    from datetime import date #se importo algo dentro da def, ela so acontece dentro da def
    ano=date.today().year
    idade=ano-num
    print(f'Você possui {idade} anos. O voto é ', end='')
    if idade < 16:
        print('NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        print('OPCIONAL')
    else:
        print('OBRIGATÓIO')


nascimento=int(input('Insira seu ano de nascimento: '))
voto(nascimento)