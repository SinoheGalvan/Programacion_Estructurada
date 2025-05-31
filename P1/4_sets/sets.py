'''

 Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados
'''

import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"Hola"}
print(varios)

#ejemplo Crear un programa que solicite los emails de los alumnos de la UTD. Almacenar en una lista y posteriormente mostrar en pantalla los emails sin duplicados.

os.system("cls")
opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame el email:  "))
    print(emails)
    opc=input("¿Deseas solicitar otro email (si/no):   ").lower()
