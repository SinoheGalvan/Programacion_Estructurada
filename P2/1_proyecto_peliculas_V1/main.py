'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar nombres de peliculas

'''
import peliculas
movies = ["Los increibles","Matrix","Mi villano favorito"]

peliculas.borrarPantalla()

op = int(input(".:: CARTELERA CINEMAX ::. \n\t\t 1. Agregar pelicula \n\t\t 2. Eliminar pelicula \n\t\t 3. Modificar pelicula \n\t\t 4. consultar pelicula "))
resp = True
peliculas.borrarPantalla()
match(op):  
    case 1:
        while resp:
            peliculas.agregar_pelicula(movies,resp)
            peliculas.EsperarTecla()
            resp = False
    case 2:
        while resp:
            peliculas.eliminar_peliculas(movies,resp)
            peliculas.EsperarTecla()
            resp = False
    case 3:
        while resp:
            peliculas.modificar_peliculas(movies,resp)
            peliculas.EsperarTecla()
            resp = False
    case 4:
        while resp:
            peliculas.consultar_peliculas(movies,resp)
            peliculas.EsperarTecla()
            resp = False
print(movies)

            


