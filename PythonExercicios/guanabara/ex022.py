frase=str(input('Digite o seu nome: ')).strip()
fmaiusculo=frase.upper()
fminusculo=frase.lower()
print(f"""Seu nome em maiúsculo é {fmaiusculo}
Seu nome em minúsculo é {fminusculo}""")

dividido=frase.split()
dividido2=''.join(dividido)
print(f"""No total possui {len(dividido2)} letras""") # ou print(f"""No total possui {len(frase) - frase.count(' ')} letras""")

dividido1=dividido[0]#primeira frase
print(f"""Seu primeiro nome possui {len(dividido1)} letras""") #ou(dividido[0],len(dividido[0])