valor=True
soma=contagem=0
while valor==True: #minha maneira
    numero = int(input('Digite um valor inteiro. Insira "999" para sair: '))
    if numero == 999:
        valor=False
    else:
        soma+=numero
        contagem+=1

"""numero = int(input('Digite um valor inteiro. Insira "999" para sair: ')) 
while numero!=999:
        soma+=numero
        contagem+=1
        numero = int(input('Digite um valor inteiro. Insira "999" para sair: '))"""

print(f'A soma de todos os número deu {soma}. Foram inseridos {contagem} números.')
