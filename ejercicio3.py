from functools import reduce
import numpy as np


# contador = 0
# nPlantas = int(input("Cuantas Plantas desea registrar 'ej : 5' : "))
# file = open("Plantas.txt" , "w")
# while contador < nPlantas:
#     file.write(input("ingrese nombre y altura en centimetros de la planta separada por una coma 'ej: planta1 , 183 ' : ") + os.linesep )
#     contador +=1
# file.close()

alturasPlantas = [] 
alturasNumericas = []

file = open("Longitudes.txt" , "w")
file.write("escarabajo1 , 120 \nescarabajo2 , 130 \nescarabajo3 , 200\nescarabajo4 , 180\nescarabajo5 , 90")
file.close()

file = open("Longitudes.txt" , "r")
listaArboles = file.readlines()

for i in listaArboles: 
    a = i.split(",")
    alturasPlantas.append(a[1])
    
for i in alturasPlantas:
    a = i.strip("\n")
    alturasNumericas.append(int(a))

promedio = (reduce(lambda a,b: a+b , alturasNumericas))/len(alturasNumericas)
desviacion = np.std(alturasNumericas)

filer = open("Resultados.txt" , "w")
filer.write('El promedio de las Longitudes de los escarabajos es: %d' %(promedio) + ' y la desviacion estandar es: %1.10f' %(desviacion))
filer.close()