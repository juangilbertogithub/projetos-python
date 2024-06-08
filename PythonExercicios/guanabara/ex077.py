"""palavras= 'casa', 'vida', 'biscoito', 'saude', 'principio'
vogais= 'a','e','i','o','u'

for c in palavras:
    print(f'\n{c}',end=' ')
    for letra in c:
        if letra.lower() in vogais:
            print(letra, end=' ')"""


palavras= 'casa', 'vida', 'biscoito', 'saude', 'principio'
vogais= 'a','e','i','o','u'

for p in palavras:
    print(f'\n{p}', end=' ')
    for letra in p:
        if letra in vogais:
            print(letra, end=' ')