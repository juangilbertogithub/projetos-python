km=float(input('Qual é a distância da sua viagem? '))
if km<=200:
    passagem=km*0.5
    print(f'Você irá fazer uma viagem de {km}km.')
    print(f'O preço da sua viagem é de R${passagem:.2f}.')
else:
    passagem = km * 0.45
    print(f'Você irá fazer uma viagem de {km}km.')
    print(f'O preço da sua viagem é de R${passagem:.2f}.')

#passagem=km*0.5 if <=200 else km*0.45