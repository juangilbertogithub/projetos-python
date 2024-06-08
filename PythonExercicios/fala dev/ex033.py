fn1=1
fn2=0
print('Os 8 primeiros termos da série de Fibonacci são:', end=' ')
for c in range(0,8):
    if c==0:
        print(fn1, end=' ')
    else:
        fn3=fn1+fn2
        print(fn3, end=' ')
        fn2=fn1
        fn1=fn3


#A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Escreva um programa que apresente 8 termos da série de Fibonacci.