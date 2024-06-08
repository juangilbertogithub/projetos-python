print('Insira sua nota entre 0 e 10.')
nota=float(input('Nota: '))
while nota < 0 or nota>10:
    print('Valor inválido. Por favor, inserir uma nota entre 0 e 10.')
    nota=float(input('Nota: '))
print(f'{nota} é um valor válido.')

#Escreva o trecho de um programa que lê e valida a nota de um aluno(0.0 ≤ nota ≤ 10.0)