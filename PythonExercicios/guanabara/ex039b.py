from datetime import date
tempo=date.today().year

anos=int(input('Digite a sua idade: '))
nascimento=tempo-anos

if anos>18:
    alistar=anos-18
    anoalistar=tempo-alistar
    print(f'Vá se alistar. Você já completou 18 anos há {alistar} anos, ou seja, deveria ter ido em {anoalistar}.')

elif anos==18:
    print('Vá se alistar nesse ano.')

elif anos<18:
    alistar = 18 - anos
    anoalistar = tempo + alistar
    print(f'Você nasceu em {nascimento}. Em {alistar} anos, ou seja, em {anoalistar} você terá 18 anos e deverá se alistar.')
