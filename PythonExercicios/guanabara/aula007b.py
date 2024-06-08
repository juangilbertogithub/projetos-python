print(1+2) #soma
print(1*2) #multiplicação
print(1/2) #divisão
print(1**3) #potencialização
print(1//2) #divisão inteira
print(1%2) #resto de divisão

pow(1,3) #potencialização de outra forma
81**(1/2) #para descobrir uma raíz

# () em primeiro
# ** em segundo
# * // / % em terceiro
# + - em quarto

print ('Oi'+ 'Olá')
print('Oi'*5)

nome=str(input('Insira seu nome: '))
print(f'Prazer em te conhecer, {nome}!')
print(f'Prazer em te conhecer, {nome:20}!') #com 20 espaços
print(f'Prazer em te conhecer, {nome:>20}!') #a direita dos 20 espaços
print(f'Prazer em te conhecer, {nome:<20}!') #a esquerda dos 20 espaços
print(f'Prazer em te conhecer, {nome:^20}!') #centralizado nos 20 espaços
print(f'Prazer em te conhecer, {nome:=^20}!') #centralizado nos 20 espaços e com simbolo de igual no resto dos espaços

n1=int(input('Insira um valor: '))
n2=int(input('Insira outro valor: '))
print(f'A soma vale {n1*n2:.3f}') #se só quero 3 casa flutuantes
# para quebrar a linha posso utilizar /n no final
#para juntar as linhas, posso utilizar , end='' no final