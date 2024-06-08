from datetime import date
ano=date.today().year

menor=maior=0

for c in range (1,8):
    nascimento=int(input(f'Digite seu ano de nascimento da {c}ª pessoa: '))
    resultado=ano-nascimento

    if resultado >= 21:
        maior+=1

    if resultado < 21: #ou else
        menor+=1

print(f'São {menor} menores de idade e {maior} maiores de idade.')