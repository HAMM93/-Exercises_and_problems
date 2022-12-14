import functools
from operator import index


numeroDePuntos = int(input("¿Cuantos puntos desea agregar a su coleccion? 'ej: 5'  : "))

contador = 0
listaCordenadas = []
listaDistancias = []

calculoDistancia = lambda a,b,c,d : ((a-c)**2 +(b-d)**2)**0.5

def distanciaMenor(lista):
    menor = functools.reduce(lambda a, b: a if a < b else b, lista)
    posicionMenor = lista.index(menor)
    menorDistancia = menor
    
    return posicionMenor, menorDistancia

while contador < numeroDePuntos:
    ordenadas= input("ingrese el valor de las ordenadas del punto, separados por una coma 'ej 5,1' :").split(',')    
    listaCordenadas.append(ordenadas)
    contador += 1
print("---------------------------------------------------------------------------------")
puntoReferencia = input("ingrese el valor de las ordenadas del punto de referencia, separados por una coma 'ej 5,1' :").split(',')     
print("------------------------------------------------------------------------------------------------")
for e in listaCordenadas:
    distancia = calculoDistancia(int(puntoReferencia[0]),int(puntoReferencia[0]),int(e[0]),int(e[1]))
    listaDistancias.append(round(distancia,10))

posicionoYvalor=distanciaMenor(listaDistancias)



print(f"La menor distancia registrada frente al punto de referencia es :  {posicionoYvalor[1]}")
print(f"La cordenadas del punto con menor distancia :  {listaCordenadas[posicionoYvalor[0]]}")