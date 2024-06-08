#lista com o nome. cada bloco de string possui um numero de 0 a infinito. posso usar a minha contagem pra selecionaar eles. as oturs n tem segredp

contidade18=0
conthomem=0
contmulhermenos20=0

while True:
    print('Cadastro')
    idade=int(input('Digite a sua idade: '))
    if idade>=18:
        contidade18 +=1

    sexo=str(input('Digite o seu sexo [H/M]: ')).strip().upper()[0]
    if sexo=='H':
        conthomem +=1
    if sexo=='M' and idade <=20:
        contmulhermenos20 += 1

    continuar=str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'''Pessoas com mais de 18 anos cadastradas: {contidade18}
      Homens cadastrados: {conthomem}
      Mulheres com menos de 20 anos cadastradas: {contmulhermenos20}''')