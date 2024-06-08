n1=float(input('Insira a sua primeira nota: '))*2
n2=float(input('Insira a sua segunda nota: '))*3
n3=float(input('Insira a sua terceira nota: '))*5
media_ponderada=(n1+n2+n3)/(2+3+5)
print(f'Você tirou {media_ponderada}')
if media_ponderada>=6:
    print('APROVADO')
else:
    print('REPROVADO')

#Elabore um programa que leia notas de três avaliações de um aluno. A primeira avaliação tem peso 2, a segunda tem peso 3
#e, a terceira, peso 5. Calcule a média do aluno. Se a média do aluno for maior ou igual a 6, o aluno está aprovado; caso
#contrário, o aluno está reprovado. Mostre o resultado da decisão.