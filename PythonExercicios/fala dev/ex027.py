alunos=int(input('Insira a quantidade de alunos que serão inseridos (de 1 a 200): '))
while alunos < 1 or alunos > 200:
    print('Valor inválido!')
    alunos = int(input('Insira a quantidade de alunos que serão inseridos (de 1 a 200): '))

contagem=aprovado=reprovado=0

while contagem < alunos:
    contagem += 1
    print(f'Nota do aluno nº{contagem}')
    n1=float(input(f'Primeira nota: '))
    n2=float(input(f'Segunda nota: '))
    while n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
        print('Valor inválido!')
        print(f'Nota do aluno nº{contagem}')
        n1=float(input(f'Primeira nota: '))
        n2=float(input(f'Segunda nota: '))
    media=(n1+n2)/2
    print(f'Média: {media:.2f}.')
    if media>=6:
        print('APROVADO')
        aprovado+=1
    else:
        print('REPROVADO')
        reprovado+=1

print(f'Alunos aprovados: {aprovado}')
print(f'Alunos reprovados: {reprovado}')

#Escreva um programa que leia duas notas de n alunos.
#Calcule e apresente:
   #- a média de cada aluno (aritmética);
   #- a quantidade de alunos aprovados (média superior ou igual a 6.0);
   #- a quantidade de alunos reprovados (média inferior a 6.0).
#Obs:
 #n será um número informado pelo usuário que representa a quantidade de alunos da turma.
 #Validar:
      #- quantidade de alunos(n): só aceitar de 1 a 200;
      #- nota: só aceitar de 0.0 a 10.0