#Para visualizar la serie dele un valor a n que corresponde a la cantidad de terminos a calcular apartie del 3
n = 10

def serie(n,a,b,c):
    if n == 0:
        return c
    else:
        return serie(n-1,b,c,a+b+c+4)


# print(serie(3,1,1,5))

for i in range(0,n):
    print(serie(i,1,-1,3))