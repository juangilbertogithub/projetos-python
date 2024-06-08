"""listageral=list()
listanome=list()
listanotas=list()
dados=list()
listamedias=list()
contagem=0

while True:
    listanome.append(str(input('Insira o nome: ')).strip().capitalize())

    nota1=int(input('Insira a primeira nota: '))
    dados.append(nota1)
    nota2=int(input('Insira a segunda nota: '))
    dados.append(nota2)
    media=(nota1+nota2)/2

    listamedias.append(media)
    listanotas.append(dados[:])

    dados.clear()

    pergunta=str(input('Deseja continuar? Sim ou não: ')).upper()[0]
    if pergunta == 'N':
        break

listageral.append(listanome[:])
listageral.append(listanotas[:])
listageral.append(listamedias[:])
#nome, notas, medias

print('NOTA DOS ALUNOS')
print('-'*30)

for c in listageral:
    print(contagem, listageral[c][0], listageral[c][1])
    contagem += 1

print('-'*30)

while True:
    nota=int(input(('De quem gostaria de ver a nota? (999 para interromper) ')))

    if nota == 999:
        break
    else:
        print(listamedias[nota])"""


ficha=list()

while True:
    nome=str(input('Digite o nome do aluno: '))
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media]) #IMPORTANTE!!! N SABIA E AJUDOU MUITO
    sair=str(input('Deseja continuar? Sim ou Não: '))[0].strip().upper()
    if sair == 'N':
        break

print(f'{"BOLETIM":^20}')
print('-'*20)
print(f'{"Número":<4} |{"Nome":<10}|{"Nota":>8}')
for indice,aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:^10}{aluno[2]:>8.1f}')#da pra fazer as duas coisas ao mesmo tempo

while True:
    nota=int(input(('De quem gostaria de ver a nota? (999 para interromper) ')))
    if nota==999:
        print('FIM')
        break
    else:
        print(f'{ficha[nota][0]}: {ficha[nota][1]}')

#refazer esse