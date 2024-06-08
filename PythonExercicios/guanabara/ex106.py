def funçao(texto): #meio bosta
    help()
    help(texto)

comando=''
while True:
    if comando.upper()=='FIM':
        break
    else:
        funçao(comando)