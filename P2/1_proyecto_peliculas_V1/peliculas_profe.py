peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print("\n\t.:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip())
  input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
  if len(peliculas)>0:
      for i in range(0,len(peliculas)):
        print(f"{i+1}.- {peliculas[i]}")
  else:
    print("\t ..:: NO HAY PELICULAS EN EL SISTEMA ::.")

def vaciarPeliculas():
  borrarPantalla()
  print("\n\t .:: Borrar o quitar TODAS las peliculas ::.")
  resp=input("¿Deseas quitar o borrar TODAS las peliculas del sistema? (Si/No)").lower()
  if resp=="si":
    peliculas.clear()
    input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def buscarPeliculas():
  borrarPantalla()
  print("\n\t .:: Buscar peliculas ::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t ¡No se encuentra la pelicula a buscar!")
  else:
    for i in range(0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"La película {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
        encontro+=1
    if encontro>0:
      print(f"\n Tenemos {encontro} pelicula(s) con este titulo")
      input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def eliminarPeliculas():
   borrarPantalla()
   print("\n\t.:: Borrar Películas ::.\n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la pelicula a buscar!")   
   else: 
      resp="si"  
      while pelicula_buscar in peliculas and resp=="si":
          resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)?").lower()
          if resp=="si":
            posicion=peliculas.index(pelicula_buscar)
            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
            peliculas.remove(pelicula_buscar) 
            encontro+=1
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      print(f"Se borro {encontro} pelicula(s) con este titulo")

def modificarPeliculas():
   borrarPantalla()
   print("\n\t.:: Modificar Películas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
             peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
             encontro+=1
             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")
      