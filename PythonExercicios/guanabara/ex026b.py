frase=str(input('Digite uma frase qualquer: ')).strip()
frasemaiuscula=frase.upper()
numero=frasemaiuscula.count('A')
print(f'A letra "A" aparece {numero} vezes na frase "{frase}".')
numero2=frasemaiuscula.find('A')
print(f'A primeira vez que aparece é na posição {numero2+1}.')
numero3=frasemaiuscula.rfind('A')
print(f'A última posição que a letra "A" aparece é na posição {frasemaiuscula.rfind("A")+1}.')