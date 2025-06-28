'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoria, clasificación, género, idioma) de las peliculas.

'''

import peliculas_profe

opcion=True
while opcion:
    peliculas_profe.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar Caracteristicas \n\t\t 5.- Modificar Caracteristicas \n\t\t 6.- Borrar Caracteristicas \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_profe.crearPeliculas()
            peliculas_profe.esperarTecla()
        case "2":
            peliculas_profe.borrarPeliculas()
            peliculas_profe.esperarTecla()  
        case "3":
            peliculas_profe.mostrarPeliculas()
            peliculas_profe.esperarTecla()     
        case "4":
            peliculas_profe.agregarCaracteristicaPeliculas()
            peliculas_profe.esperarTecla()
        case "5": 
            peliculas_profe.modificarCaracteristicaPeliculas()
            peliculas_profe.esperarTecla() 
        case "6": 
            peliculas_profe.borrarCaracteristicaPeliculas()
            peliculas_profe.esperarTecla() 
        case "7":
            opcion=False
            peliculas_profe.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")