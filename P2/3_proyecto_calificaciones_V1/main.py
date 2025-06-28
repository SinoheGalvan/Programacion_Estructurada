'''
Proyecto 3
Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menú de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante.

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como sus tres calificaciones.

'''

import calificaciones

def main():

    datos = []

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
    
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()  
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()     
            case "4":
                opcion=False
                calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion=True 
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()