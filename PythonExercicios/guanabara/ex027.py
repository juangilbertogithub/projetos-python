'''nome=str(input('Digite o seu nome: ')).strip()
nomediv=nome.split()
print(f'Seu primeiro nome é {nomediv[0]} e seu último nome é {nomediv[len(nomediv)-1]}.')'''

nome=str(input('Digite o seu nome: ')).strip()
n=nome.split()
print(f'Seu primeiro nome é {n[0]} e seu último nome é {n[-1]}.')