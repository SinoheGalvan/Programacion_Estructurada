import os

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[23,45,56,78]

print(numeros)

for i in numeros:
    print(i)

for i in range(0,len(numeros)):
    print(numeros[i])


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

os.system("cls")
palabras=["HOLA","DESPIDO","ARTEMISA","VALLE MUERTE"]

p_buscar=input("Ingresa la palabra a buscar:\n").upper()

#1ra forma (Solo busca la palabra 1 vez)
if p_buscar in palabras:
    print(f"Si encontre la palabra")
    print(f"El numero de veces que se encontro la palabra es: {palabras.count(p_buscar)}")
else:
    print(f"No encontre la palabra")

#2da forma (Encuentra la palabra)
encontro=False
for i in palabras:
    if i == p_buscar:
        encontro=True

if encontro:
    print(f"Si encontre la palabra")
else:
    print(f"No encontre la palabra")

#3er forma
found=False
for i in range(0,len(palabras)):
    if palabras[i] == p_buscar:
        found=True

if found:
    print(f"Encontre la palabra")
else:
    print(f"NO encontre la palabra")


input("Oprima tecla....")

#Ejemplo 3 Añadir elementos a la lista

os.system("cls")
numeros=[]
print(numeros)

option=True
while option:
    numero=float(input("Dame un numero entero o decimal:"))
    numeros.append(numero)
    resp=input("¿Deseas agregar otro numero?").lower()
    if resp=="si":
        option=True
    else:
        option=False

print(numeros)
input("Oprima tecla....")

#Ejemplo 4 crear una lista multidimensional que sea una agenda

agenda=[
    ["Carlos",6181234567],
    ["Alberto",6671234567],
    ["Martin",6785678923]
    ]

print(agenda)

for i in agenda:
    print(i)

cadena=""
for r in range(0,3):
    for c in range(0,2):
        #print(agenda[r][c])
        cadena+=f"{agenda[r][c]}   "
    cadena+="\n"
print(cadena)



