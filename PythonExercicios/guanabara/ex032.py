from datetime import date
ano=int(print('Digite um ano para saber se ele é bissexto. Para saber o seu ano, digite 0: '))
if ano==0:
    ano=date.today().year #pega o ano atual e joga embaixo
if ano %4==0 and ano%100!=0 or ano%400==0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
