import datetime
s1=0
s2=0
for c in range (1,8):
    n=int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    ano=datetime.date.today().year-n
    if ano>18:
        s1=s1+1
    if ano<18:
        s2=s2+1
print(f'{s1} pessoas possuem mais de 18 anos. \n{s2} pessoas possuem menos de 18 anos.')