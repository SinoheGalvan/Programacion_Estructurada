from funciones import *
from exportar import *
from clientes import cliente
from apartamentos import apartamento

def main():
    opcion = True
    while opcion:
        borrarPantalla()
        print(  "\n\t     ..:::   Sistema informático en consola para    :::..." 
                "\n\t..:::🏠 la administración de apartamentos/locales en renta 🏠:::..." 
                "\n\t 1.- 👤 Clientes" 
                "\n\t 2.- 🏢 Apartamentos"
                "\n\t 3.- 📄 Exportar"
                "\n\t 4.- 🚪 Salir" )
        rsp=input("\t\t 👉 Elige una opción: ").upper()
        match rsp:
            case "1":
                main_clientes()
            case "2":
                main_apartamentos()
            case "3":
                main_documentos()
            case "4":
                opcion = False
                borrarPantalla()
                print("✅ Cerrando el programa...")

def main_clientes():
    borrarPantalla()
    opcion= True
    while opcion:
        rsp = menu_Clientes()
        match rsp:
            case "1":
                cliente.agregarRegistro()
            case "2":
                cliente.modificarRegistro()
            case "3":
                cliente.buscarRegistro()
            case "4":
                cliente.borrarRegistro()
            case "5":
                cliente.mostrarRegistro()
            case "6":
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción inválida, vuelva a intentarlo... por favor 📛")

def main_apartamentos():
    borrarPantalla()
    opcion= True
    while opcion:
        rsp = menu_Apartamentos()
        match rsp:
            case "1":
                apartamento.agregarRegistro()
            case "2":
                apartamento.modificarRegistro()
            case "3":
                apartamento.buscarRegistro()
            case "4":
                apartamento.borrarRegistro()
            case "5":
                apartamento.mostrarRegistro()
            case "6":
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción inválida, vuelva a intentarlo... por favor 📛")

def main_documentos():
    borrarPantalla()
    opcion= True
    while opcion:
        formato = menu_exportar()
        match formato:
            case "1":
                exportarPDF()
            case "2":
                exportarXlsx()
            case "3":
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción invalida vuelva a intentarlo ... por favor 📛")

if __name__=="__main__":
    main() 

