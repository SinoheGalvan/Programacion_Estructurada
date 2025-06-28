import peliculas_profe

opcion=True
while opcion:
    peliculas_profe.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_profe.agregarPeliculas()
            peliculas_profe.esperarTecla()
        case "2":
            peliculas_profe.eliminarPeliculas()
            peliculas_profe.esperarTecla()  
        case "3":
            peliculas_profe.modificarPeliculas()
            peliculas_profe.esperarTecla()     
        case "4":
            peliculas_profe.consultarPeliculas()
            peliculas_profe.esperarTecla()
        case "5": 
            peliculas_profe.buscarPeliculas()
            peliculas_profe.esperarTecla() 
        case "6": 
            peliculas_profe.vaciarPeliculas()
            peliculas_profe.esperarTecla() 
        case "7":
            opcion=False
            peliculas_profe.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")