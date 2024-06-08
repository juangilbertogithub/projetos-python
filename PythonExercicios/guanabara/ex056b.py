homem=[]
idadetotal=0
mmenos20=0
maioridadehomem=0
homemmaisvelho=''

for c in range (1,5):
    nome=str(input('Digite seu nome: ')).strip().capitalize()
    idade=int(input('Digite a sua idade: '))
    idadetotal+=idade
    sexo=str(input('Digite seu sexo: '))[0].upper().split()
    
    if sexo == 'M':
        if idade > maioridadehomem:
            maioridadehomem=idade
            homemmaisvelho=nome

    if sexo == 'F':
        if idade <20:
            mmenos20+=1

media=idadetotal/c

print(f'A média de idade do grupo é de {media:.0f} anos.')
print(f'Do grupo, {mmenos20} mulheres possuem menos de 20 anos.')
print(f'O nome do homem mais velho é: {homemmaisvelho}.')