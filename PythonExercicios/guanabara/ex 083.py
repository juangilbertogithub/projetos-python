#insiro a expressao
#jogo em uma lista
#faço um for q adiciona um numero a cada ( ou ) que encontra
#faço um len par ou impar dizendo se ta certo ou errado #nao pq posso ter 2 (( ou 2 )) e ele pensar q ta certo
#posso buscar pelas ( ou ). se a quantidade de ( encontrados for igual a de ) encontrados, é valido. caso contrario, invalido.

"""lista=[]
parentesesesquerda=[]
parentesesdireita=[]

expressao=str(input('Insira uma expressão matemática: ')).strip()
lista.append(expressao)

for frase in lista:
    #print(frase)
    for letras in frase:
        #print(letras)
        if '(' in letras:
            parentesesesquerda.append(letras)
        if ')' in letras:
            parentesesdireita.append(letras)

#print(parentesesdireita)
#print(parentesesesquerda)

if len(parentesesdireita) == len(parentesesesquerda):
    print('Sua expressão está certa!')

#if len(parentesesdireita) != len(parentesesesquerda):
else:
    print('Sua expressão está errada!')"""



lista=[]
parentesesesquerda=[]
parentesesdireita=[]
lista.append(str(input('Insira uma expressão matemática: ')).strip())
for frase in lista:
    for letras in frase:
        if '(' in letras:
            parentesesesquerda.append(letras)
        if ')' in letras:
            parentesesdireita.append(letras)
print('Sua expressão está certa!') if len(parentesesdireita) == len(parentesesesquerda) else print('Sua expressão está errada!')