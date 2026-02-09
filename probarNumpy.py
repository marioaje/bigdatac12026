import numpy as npUsarLibreria

# son vectores, listas de datos, arreglos
lista = [ 1, 3, 4]
listados = [ 1, 3, 4]
print(lista)
print(listados)

lista = [ x * 2 for x in lista ]
resultadoArreglo = npUsarLibreria.array([ 1, 3, 4])
resultadoArreglo * 2

print(lista)
print(listados)
print(resultadoArreglo * 2)


#Ejemplo de division

declaramosVarible = npUsarLibreria.array([10,20, 30])
print(declaramosVarible)
print(declaramosVarible/5)