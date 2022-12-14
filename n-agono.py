
import numpy as np

cicloActivo = True

def calcAngulo(n):
    return ((np.pi)/(n))

def calcApotema(hipo,alpha):
    return((hipo)*(np.cos(alpha)))

def calculoCateOpu(hipo,alpha):
    return((hipo)*(np.sin(alpha)))

while cicloActivo:
    print("--------------------------------------Poligonos--------------------------------------")
    nLados = int(input("Ingrese el numero de lados de su poligono 'ej : 6' : "))
    hipotenusa = float(input("Ingrese (en cm) el valor de la distancia entre el centro y un vertice 'ej : 13' : "))
    print("--------------------------------------Resultado--------------------------------------")
    
    angulo = calcAngulo(nLados)
    catetoOpuesto = calculoCateOpu(hipotenusa,angulo)
    apotema = calcApotema(hipotenusa,angulo)
    lado = 2 * catetoOpuesto 
 
    perimetroG = lambda a, b : a*b
    areaPoligonoG = lambda a, b : (a*b)/2
    
    perimetro = perimetroG(lado,nLados)
    areaPoligono = areaPoligonoG(perimetro,apotema)

    print(f"El poligono de {nLados} lados, tiene un perimetro de {perimetro} cm")
    print(f"y su Area es de {areaPoligono} cm cuadrados")
        
    print("-------------------------------------------------------------------------------------")
    apagarCiclo = input("¿Desea calcular otro poligono? (si o no) : ")
    if apagarCiclo == "si" or apagarCiclo == "Si":
        cicloActivo = True
    elif apagarCiclo == "no" or apagarCiclo == "No":
        cicloActivo = False
        print("----------------------------------Fin del programa------------------------------------")
    else:
        print("eleccion Invalida el programa finalizara")
        cicloActivo = False
        print("----------------------------------Fin del programa------------------------------------")