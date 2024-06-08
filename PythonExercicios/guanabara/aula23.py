try:
    a=int(input('Digite o Numerador: '))
    b=int(input('Digite o Denominador: '))
    r=a/b

except: #so estou conseguindo executar um por vez
    print('Infelizmente, tivemos um problema :(')

#except Exception as erro:
    #print(f'O problema encontrado foi {erro.__cause__}.')

#expect (ValueError,TypeError): #n funciona por algum motivo
    #print('Tivemos um problema com os tipos de dados que você digitou.')


else:
    print(f'O resultado é {r}.')

finally: #opcional
    print('Obrigado, volte sempre.')