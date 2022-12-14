import functools

numeroDePuntos = int(input("¿Cuantos vertices desea ingresar en su cadena? 'ej: 5'  : "))

contador = 0
listaCordenadas = []
listaDistancias = []

calculoDistancia = lambda a,b,c,d : ((a-c)**2 +(b-d)**2)**0.5

while contador < numeroDePuntos:
    ordenadas= input("ingrese el valor de las ordenadas del vertice, separados por una coma ej 5,1 :").split(',')    
    listaCordenadas.append(ordenadas)
    contador += 1
    

for c in range(len(listaCordenadas)-1):
    puntoA = listaCordenadas[c]
    puntoB = listaCordenadas[c+1]
    valor = (calculoDistancia(int(puntoA[0]),int(puntoA[1]),int(puntoB[0]),int(puntoB[1])))
    listaDistancias.append(round(valor,10)) 

 

distanciaTotal = functools.reduce(lambda a, b: a+b, listaDistancias)
print("la suma de las distancias que componen la cadena poligonal es : ", end="")   
print(distanciaTotal)  



