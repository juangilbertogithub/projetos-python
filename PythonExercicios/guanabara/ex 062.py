print('Contagem dos 10 primeiros de uma P.A.') #um pouco confuso como funciona
a=int(input('Insira o primeiro termo: '))
r=int(input('Insira a sua razão: '))
novoa=0
c=1
total=0
mais=10

while mais!=0:
    total+=mais

    while c<=total: #pq ele continua do mais? como ele n conta td de novo desde o 0?
        print(a) #esse começa como o primeiro aparecendo, por isso o c começa como 1 antes de somar
        c+=1
        a+=r
    mais=int(input('Mais quantos termos gostaria de pular? '))
print('fim')

"""print('Contagem dos 10 primeiros de uma P.A.')

a=int(input('Escolha o primeiro termo: '))
r=int(input('Escolha uma razão: '))
n=a #n = a + (10) * r quando usava o for. tive q dar um novo termo pq se n ele n iria funcionar por pensar q iria inserir um novo valor?
c=1
total=0
mais=10 #pq sao de 10 termos e a contagem ja contou os 10 iniciais

while mais !=0:
    total=total+mais
    while c<=total:
        print(f'{n}', end=' > ')
        c += 1
        n += r

    print('PAUSA')
    mais=int(input('Mais quantos termos gostaria que mostrasse a mais? '))

print(f'{total} termos totais mostrados.')
print('FIM')"""