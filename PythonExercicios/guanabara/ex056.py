maiorhomem=0
contmenor=0
idadesom=0
mediaidade=0
nomehomem='' #eu tinha colocado 0 e dava 0 como resultado

for c in range (1,5):
    nome=str(input('Digite seu nome: ')).strip().capitalize()
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo (M ou F): ')).strip().upper()
    idadesom=idadesom+idade
    if sexo == 'M':
        if c == 1: #eu tinha colocado que a idade == 0
            maiorhomem = idade #eu tinha colocado ==. estava dando 0 por causa disso
            nomehomem = nome #nao tinha definido o nome do cara nesse if. apenas tinha colocado no if seguinte. por isso n funcionava
        if maiorhomem > idade:
            maiorhomem = idade
            nomehomem = nome
    if sexo == 'F':
        if idade <= 20:
            contmenor+=1
        else:
            contmenor='Nenhuma'

idademedia=idadesom/c
print(f'A média de idade do grupo é de {idademedia} anos.')
print(f'O homem com a maior idade se chama {nomehomem} e tem {maiorhomem} anos.')
print(f'{contmenor} mulheres possuem menos de 20 anos.')