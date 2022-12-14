import functools
from operator import index


numeroDePuntos = int(input("¿Cuantos puntos desea agregar a su coleccion? 'ej: 5'  : "))

contador = 0
listaCordenadas = []
listaDistanciasA = []
listaDistanciasB = []

calculoDistancia = lambda a,b,c,d : (((a-c)**2) +((b-d)**2))**0.5

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
puntoReferenciaA = input("ingrese el valor de las ordenadas del punto de referencia A, separados por una coma 'ej 5,1' :").split(',')     
print("------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------")
puntoReferenciaB = input("ingrese el valor de las ordenadas del punto de referencia B, separados por una coma 'ej 5,1' :").split(',')     
print("------------------------------------------------------------------------------------------------")

for e in listaCordenadas:
    distancia = calculoDistancia(int(puntoReferenciaA[0]),int(puntoReferenciaA[1]),int(e[0]),int(e[1]))
    listaDistanciasA.append(round(distancia,10))

for e in listaCordenadas:
    distancia = calculoDistancia(int(puntoReferenciaB[0]),int(puntoReferenciaB[1]),int(e[0]),int(e[1]))
    listaDistanciasB.append(round(distancia,10))

posicionoYvalorA=distanciaMenor(listaDistanciasA)
posicionoYvalorB=distanciaMenor(listaDistanciasB)


print(listaDistanciasA)
print(listaDistanciasB)

# print(f"La menor distancia registrada frente al punto de referencia es :  {posicionoYvalor[1]}")
print(f"La cordenadas del punto mas proximo a 'A' son:  {listaCordenadas[posicionoYvalorA[0]]}")

print(f"La cordenadas del punto mas proximo a 'B' son:  {listaCordenadas[posicionoYvalorB[0]]}")