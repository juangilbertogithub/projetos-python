x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
fim=len(x)-1
for i in range(len(x)//2):
    x[i], x[fim] = x[fim], x[i]
    fim -= 1
print(x)

