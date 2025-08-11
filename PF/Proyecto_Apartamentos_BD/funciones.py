from tabulate import tabulate
from xlsxwriter import Workbook


def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\n\t\t 🕓Ingrese enter para continuar🕓")

def menu_Clientes():
    borrarPantalla()
    print(
            "\n\t..::: Administración de clientes :::..." 
            "\n\t 1.- ➕  Agregar" 
            "\n\t 2.- ✏️   Modificar"
            "\n\t 3.- 🔍  Buscar" 
            "\n\t 4.- 🗑️   Eliminar"
            "\n\t 5.- 📋  Mostrar todos"
            "\n\t 6.- 🚪  Salir ")
    rsp=input("\t\t 👉Elige una opción: ").upper()
    return rsp
    
def menu_Apartamentos():
    borrarPantalla()
    print(
            "\n\t🏢..::: Administración de apartamentos :::...🏢" 
            "\n\t 1.- ➕  Agregar" 
            "\n\t 2.- ✏️   Modificar"
            "\n\t 3.- 🔍  Buscar" 
            "\n\t 4.- 🗑️   Eliminar"
            "\n\t 5.- 📋  Mostrar todos"
            "\n\t 6.- 🚪  Salir ")
    rsp=input("\t\t 👉Elige una opción: ").upper()
    return rsp
    