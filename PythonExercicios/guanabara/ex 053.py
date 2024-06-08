frase=str(input('Digite uma frase: ')).upper().strip()

palavras=frase.split()
junto=''.join(palavras)
inverso=''
numero=len(junto)

for letra in range (numero-1,-1,-1): #vai pegar o numero de letras -1 por causa do 0 e depois vai voltar contando a partir do -1 q é antes da primeira pq a primeira é 0 e vai voltar contando
    inverso = inverso+junto[letra]
    if junto==inverso: #pq ele reconheceu q era invertido?
        palindromo='É'
    else:
        palindromo='NÃO É'

print(f'A frase "{junto}" ao contrário é {inverso}. Sua frase {palindromo} um palíndromo.')

"""frase=str(input('Digite uma frase: ')).upper().strip()
palavras=frase.split()
junto=''.join(palavras)
inverso = junto[::-1]
if junto==inverso:
    print('SIM')
else:
    print('NAO')"""
