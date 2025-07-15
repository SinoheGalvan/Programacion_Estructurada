'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoria, clasificación, género, idioma) de las peliculas.
3.- Utilizar e implementar una BD para gestionar las peliculas
'''

import peliculas_profe

opcion=True
while opcion:
    peliculas_profe.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Modificar \n\t\t 5.- Buscar \n\t\t 6.- SALIR ")
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
            peliculas_profe.modificarPeliculas()
            peliculas_profe.esperarTecla()
        case "5":
            peliculas_profe.buscarPeliculas()
            peliculas_profe.esperarTecla()
        case "6":
            opcion=False
            peliculas_profe.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")