valor=float(input('Insira o valor do produto\nR$'))
desconto=valor-(valor*0.05)

print(f'Você recebeu um desconto de 5%. Agora seu produto irá custar R${desconto:.2f}')