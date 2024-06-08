palavras=('Juan', 'Fabio')
vogais='a','e','i','o','u'

for p in palavras:
#analisei a lista dentro da lista
   for letra in p:

       if letra in vogais: #ou if letra in 'aeiou'
           print(letra, end=' ')