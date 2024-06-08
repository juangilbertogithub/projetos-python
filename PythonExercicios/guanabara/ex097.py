"""def soma(msg):
    s=0
    for c in msg:
        s+=1
    print('-'*(s+2))


def escreva(msg):
    soma(msg)
    print(msg)
    soma(msg)"""


def escreva(msg):
    tam=len(msg)+4 #maneira mais facil de fazer. tem q escrever um pouco diferente do q eu tava imaginando de por direto o len na parte debaixo
    print('-'*tam)
    print(f'  {msg}')
    print('-' * tam)


msg=str(input('Insira uma mensagem: ')).strip()
escreva(msg)