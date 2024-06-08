frase=str(input('Descubra se a frase é um palíndromo: ')).strip().upper()
separa=frase.split() #separa
junta=''.join(separa) #junta de novo
inverso='' #pode inverso=junto[::-1]
numero=len(junta)

for letra in range (len(junto)-1,-1,-1): #letra por letra invertido
    inverso+=junta[letra] #coloca invertido na lista
    if inverso==junta: #resposta
        palindromo='É'
    else:
        palindromo='NÃO É'

print(f'A frase "{frase}" {palindromo} um palíndromo. {inverso}.')

'''lista=[frase]
listainvertida=frase[::-1]
if lista==listainvertida:
    print('As frase é')
else:
    print('A frase não é')'''

#exercicio estranho, diferente.