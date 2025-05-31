'''

List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace un indice numerico.

Nota: sus valores si son modificables

La lista es una colección ordenada y modificable. Permite miembros duplicados.

'''
import os
os.system("cls")

#Funciones más comunes en las listas

paises=["México","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o Ingresar o Insertar elementos a una lista

#1er forma 
print(paises)
paises.append("Honduras")

#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Borrar o Quitar elementos de una lista

#1er forma con el index
paises.pop(1)
print(paises)

#2da forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista

#1er forma
resp="Brasil" in paises
if resp:
    print("Si encontre el país")
else:
    print("No encontre el país")

#2da forma
pais_buscar=input("Dame el pais a buscar")
for i in range (0,len(paises)):
    if paises[i] == pais_buscar:
        print("Si encontre el país")
    else:
        print("No encontre el país")

#Cuantas veces aparece un elemento dentro de una lista
print(f"Este número aparece: {numeros.count(12)} vez(ces)")

numeros.append(12)
print(f"Este número 12 aparece: {numeros.count(12)} vez(ces)")

#Identificar o conocer el indice de un valor

indice=paises.index("España")
print(indice)

paises.pop(indice)
print(paises)

#Recorrer los valores de una lista

#1er forma (valores)
for i in paises:
    print(i)

#2da forma (indices)
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#Unir contenido de listas
print(paises)
print(numeros)

paises.extend(numeros)
print(paises)