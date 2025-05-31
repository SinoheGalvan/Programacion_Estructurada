# Un módulo es simplemente un archivo con extensión. py que contiene código de Python (funciones, clases, variables, etc.). 

import os

def solicitar():
    nombre = input("Ingrese su nombre")
    telefono = input("Ingrese su telefono")
    print("Función 1")
    print(f"Nombre: {nombre}"
          f"\n Telefono: {telefono}")

def solicitar_3(nombre,telefono):
    print("Función 3")
    print(f"Nombre: {nombre}"
          f"\n Telefono: {telefono}")

def solicitar_2(nombre,telefono):
    print("Función 2")
    nombre = input("Ingrese su nombre")
    telefono = input("Ingrese su telefono")
    return (f"Nombre: {nombre}\n Telefono: {telefono}")
  
def solicitar_4(nombre,telefono):
    print("Función 4")
    nom = nombre
    tel = telefono
    return nom,tel

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input(".:: Oprima una tecla para continuar ::..")

def saludar(nombre):
    nom=nombre
    return f"\t¡Hola, bienvenido: {nom}!\n"