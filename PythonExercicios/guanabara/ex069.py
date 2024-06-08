contagemhomem=contagemmulhermenosde20=maioresde18=0
while True:

    idade=int(input('Digite a idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).upper().strip()[0]
        if sexo == 'M':
            contagemhomem += 1
        if idade > 18:
            maioresde18 += 1
        if sexo == 'F' and idade<20:
            contagemmulhermenosde20 +=1
    resposta= ' '
    resposta=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        if resposta =='N':
            break

print(f'Há {maioresde18} pessoas maiores de 18 anos. Há {contagemhomem} homens foram cadastrados. Há {contagemmulhermenosde20} de mulheres com menos de 20 anos.')