#nao consegui

numero=int(input('Digite um número de 3 dígitos: '))
"""lista=(str(numero))
for c in lista(0,len(lista),-1):
    print(c,end='')"""
centena=numero//100
dezena=(numero%100)//10
unidade=numero%10
print(unidade,dezena,centena)

#Leia um número de 3 dígitos, determine e apresente o número invertido (exemplo: número informado = 123, número apresentado = 321).