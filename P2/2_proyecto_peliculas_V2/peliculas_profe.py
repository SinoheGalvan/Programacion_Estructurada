#peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, género, idioma)

#peliculas={
#          "nombre":"",
#          "categoria":"",
#          "clasificacion":"",
#          "genero":"",
#          "idioma":""
#}

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("Oprima cualquier tecla para continuar ...")  

def crearPeliculas():
  borrarPantalla()
  print("\n\t.:: Alta de Peliculas ::. \n")
  pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingresa el categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingresa el clasificacion: ").upper().strip()})
  pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
  print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consulta o Mostrar la pelicula ")
  if len(pelicula)>0:
    for i in pelicula:
      print(f"\t {(i)} : {pelicula[i]}")
  else:
    print("\t .:: No hay peliculas en el sistema ::.")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t .:: Borrar o Quitar TODAS las peliculas ::.")
  resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (Si/No)")
  if resp=="si":
    pelicula.clear()
    input("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO :::")
  
def agregarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t .:: Agregar Caracteristica a Peliculas ::. \n")
  atributo=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
  valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
  #pelicula.update({atributo:valor})
  pelicula[atributo]=valor

# def modificarCaracteristicaPeliculas():
#   borrarPantalla()
#   print("\n\t .:: Modificar Caracteristica a Peliculas ::. \n")
#   caracteristica=input("Introduce la caracteristica a modificar: ").lower().strip()
#   valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
#   for i in pelicula:
#     pelicula[caracteristica]=valor
#   #pelicula.update({atributo:valor})
  
# def borrarCaracteristicaPeliculas():
#   borrarPantalla()
#   print("\n\t .:: Borrar Caracteristica a Peliculas ::. \n")
#   caracteristica=input("Ingresa la caracteristica que deseas borrar: ").lower().strip()
#   #for i in pelicula:
#   del pelicula[caracteristica]

def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.::\U0001F501 Modificar Caracteristicas a Peliculas \U0001F501::. \n")
  if len(pelicula)>0:
    print(f"\n\tValores actuales: \n ")
    for i in pelicula:
      print(f"\t {i} : {pelicula[i]}")
      resp = input(f"\t ¿Deseas cambiar el valor de {i}? (Si/No)")
      if resp == "si":
        pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705 :::")
        esperarTecla()
        borrarPantalla()
  else:
    print("\n\t\t ::: \u26A0 No hay peliculas en el sistema \u26A0 :::")
    esperarTecla()

def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.::\U0001F4DB Borrar Caracteristicas a Peliculas \U0001F4DB::. \n")
  if len(pelicula)>0:
    print("\n\tValores actuales: \n ")
    for i in pelicula:
      print(f"\t {i} : {pelicula[i]}")
    resp=input(f"\t¿Deseas borrar una caracteristica? (Si/No) ")
    if resp=="si":
      atributo=input("Escribe la caracteristica que deseas borrar o quitar: ")
      pelicula.pop(atributo)
      print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705 :::")
      esperarTecla()
      borrarPantalla()
  else:
    print("\n\t\t ::: \u26A0 No hay peliculas en el sistema \u26A0 :::")
    esperarTecla()


#def consultarPeliculas():
#  borrarPantalla()
#  print("\n\t.:: Consultar Peliculas ::.")
#  if len(peliculas)>0:
#      for i in range(0,len(peliculas)):
#        print(f"{i+1}.- {peliculas[i]}")
#  else:
#    print("\t ..:: NO HAY PELICULAS EN EL SISTEMA ::.")

#def vaciarPeliculas():
#  borrarPantalla()
#  print("\n\t .:: Borrar o quitar TODAS las peliculas ::.")
#  resp=input("¿Deseas quitar o borrar TODAS las peliculas del sistema? (Si/No)").lower()
#  if resp=="si":
#    peliculas.clear()
#    input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

#def buscarPeliculas():
#  borrarPantalla()
#  print("\n\t .:: Buscar peliculas ::.")
#  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
#  encontro=0
#  if not(pelicula_buscar in peliculas):
#    print("\n\t\t ¡No se encuentra la pelicula a buscar!")
#  else:
#    for i in range(0,len(peliculas)):
#      if pelicula_buscar==peliculas[i]:
#        print(f"La película {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
#        encontro+=1
#    if encontro>0:
#      print(f"\n Tenemos {encontro} pelicula(s) con este titulo")
#      input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

#def eliminarPeliculas():
#   borrarPantalla()
#   print("\n\t.:: Borrar Películas ::.\n")
#   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
#   encontro=0
#   if not(pelicula_buscar in peliculas): 
#      print("\n\t\t ¡No se encuentra la pelicula a buscar!")   
#   else: 
#      resp="si"  
#      while pelicula_buscar in peliculas and resp=="si":
#          resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)?").lower()
#          if resp=="si":
#            posicion=peliculas.index(pelicula_buscar)
#            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
#            peliculas.remove(pelicula_buscar) 
#            encontro+=1
#            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
#      print(f"Se borro {encontro} pelicula(s) con este titulo")

#def modificarPeliculas():
#   borrarPantalla()
#   print("\n\t.:: Modificar Películas ::. \n")
#   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
#   encontro=0
#   if not(pelicula_buscar in peliculas): 
#      print("\n\t\t ¡No se encuentra la película a buscar!")   
#   else:   
#      for i in range(0,len(peliculas)):
#        if pelicula_buscar==peliculas[i]:
#          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
#          if resp=="si":
#             peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
#             encontro+=1
#             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
#      
#      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")
      