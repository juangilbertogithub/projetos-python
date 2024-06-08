from datetime import date

ano=int(input('Digite seu ano de nascimento: '))
data=date.today().year
idade=data-ano
alistamento=idade-18

if idade==18:
    print(f'Este é o seu ano de alistamento. Não esqueça de ir.')

elif idade<18:
    print(f'Acalme-se. O alistamento é apenas aos 18 anos. Você ainda possui {(-1*alistamento)} anos.')

elif idade>18:
    print(f'Você está atrasado para o seu alistamento. Deveria ter sido feito com 18 anos, ou seja, {alistamento} anos atrás. Faça seu alistamento o mais breve possível.')