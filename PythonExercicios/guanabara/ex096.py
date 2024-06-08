def area(largura,altura):
    s=largura*altura
    print(f'A área é de {largura} x {altura} é de {s:.2f}m^2.')


larg=float(input(f'Insira a largura (em metro): '))
compr=float(input(f'Insira a altura (em metro): '))
area(larg,compr)