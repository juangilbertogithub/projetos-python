'''frase=str(input('Digite o seu nome: '))
print(frase.upper())
print(frase.lower())
dividido=frase.split()
dividido1=dividido[0]#quantas letras na primeira frase
print(len(dividido1))
dividido2=''.join(dividido)
print(len(dividido2))'''

'''frase=int(input('Digite um número de 0 a 9999: '))
fraseb=str(frase)
n1=(fraseb[0])
n2=(fraseb[1])
n3=(fraseb[2])
n4=(fraseb[3])
print(f'milhar: {n1}\ncentena: {n2}\ndezena: {n3}\nunidade: {n4}')'''

'''cidade=str(input('Digite o nome da sua cidade: '))
print(f'A cidade {cidade} possui ''SANTO'' no começo do nome?')
dividido=cidade.split()
dividido1=dividido[0] #primeiro palavra da frase
dividido2=dividido1.upper() #maiusculo
print('SANTO' in dividido2)'''

'''nome=str(input('Digite seu nome: '))
print('Seu nome possui ''SILVA''?')
dividido=nome.upper().split()
print('SILVA' in dividido)'''

'''nome=str(input('Escreva algo: ').upper().strip())
print(f"""A letra A aparece {nome.count("A")} vezes.
Na primeira vez ela aparece na posição {nome.find("A")+1}
Na ultima vez ela aparece na posição {nome.rfind("A")+1}""")'''

nome=str(input('Digite o seu nome completo: '))
nomeb=nome.split()

print(f"""
Seu primeiro nome é {l.nomeb}
Seu último nome é {}
""")