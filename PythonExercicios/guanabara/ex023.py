'''frase=int(input('Digite um número de 0 a 9999: '))
fraseb=str(frase)
n1=(fraseb[0])
n2=(fraseb[1])
n3=(fraseb[2])
n4=(fraseb[3])
print(f"""milhar: {n1}
centena: {n2}
dezena: {n3}
unidade: {n4}""")'''

'''num=int(input('Digite um número de 0 a 9999: '))
n=str(num)
print(f"""milhar: {(n[3])}
centena: {(n[2])}
dezena: {(n[1])}
unidade: {(n[0])}""")'''

num=int(input('Digite um número de 0 a 9999: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print(f"""Milhar: {m}
Centena: {c}
Dezena: {d}
Unidade: {u}""")