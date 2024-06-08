frase=str(input('Digite uma frase: ')).strip().upper()
ax=frase.count('A')
print(f'A letra A aparece {ax} vezes na frase')
a1=frase.find('A')+1
print(f'A primeira letra A apareceu na posição {a1}')
a2=frase.rfind('A')+1
print(f'A última letra A apareceu na posição {a2}')