"""  
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre particular como un 
programa mas pequeño que cumple ua funcion especifica. 
La funcion se puede reutilizar con el simple hecho de invocarla es decir mandarela a llamar

Sintaxis
    def nombre(parametros):
        bloque o conjunto de instrucciones

    nombre(parametros)
    Las  funciones pueden ser de 4 tipos:
        Procedimiento
        1.-No recibe parametros y no regresa valor
        2.-No recibe parametros y regresa valor
        3.-Recibe parametros y no regresa valor
        Función
        4.-Recibe parametros y regresa valor
"""

#1.-
def solicitar():
    nombre = input("Ingrese su nombre")
    telefono = input("Ingrese su telefono")
    print("Función 1")
    print(f"Nombre: {nombre}"
          f"\n Telefono: {telefono}")

#3.-
def solicitar_3(nombre,telefono):
    print("Función 3")
    print(f"Nombre: {nombre}"
          f"\n Telefono: {telefono}")

#2.-
def solicitar_2(nombre,telefono):
    print("Función 2")
    nombre = input("Ingrese su nombre")
    telefono = input("Ingrese su telefono")
    return (f"Nombre: {nombre}\n Telefono: {telefono}")
  
#4.-
def solicitar_4(nombre,telefono):
    print("Función 4")
    nom = nombre
    tel = telefono
    return nom,tel
