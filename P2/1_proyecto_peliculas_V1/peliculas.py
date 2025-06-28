import os


def borrarPantalla():
    os.system("cls")    

def EsperarTecla():
    input("Presione para continuar...")

def agregar_pelicula(movies,r,resp):
    addPelicula = str(input("Ingresa el nombre de la pelicula a añadir: \n"))
    movies.append(addPelicula)
    print("Pelicula agregada exitosamente.\n")
    
    return movies, r , resp

def eliminar_peliculas(movies,r,resp):
    print("Seleccione la pelicula a borrar: \n")
    for i in range(0,len(movies)):
        print(f"{i}.- {movies[i]}")
    opcion = int(input())
    movies.pop(opcion)
    borrarPantalla()
    print("Pelicula borrada exitosamente. \n")
    
    return movies, r, resp

def modificar_peliculas(movies,r,resp):
    print("Selecciona la pelicula a cambiar: \n")
    for i in range(0,len(movies)):
        print(f"{i}.- {movies[i]}")
    change = int(input())
    borrarPantalla()
    oPelicula = input("Ingresa el cambio: \n")
    movies[change] = oPelicula
    r = input("Cambio realizado exitosamente. \n").upper()
    if r != "S":
        resp = False
    
    return movies, r, resp

def consultar_peliculas(movies,resp):
    print("Estas son las peliculas guardadas: \n")
    for i in range(0,len(movies)):
        print(f"{i}.- {movies[i]}")
    resp = False

