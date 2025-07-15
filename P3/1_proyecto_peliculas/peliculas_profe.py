#peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, género, idioma)

#peliculas={
#          "nombre":"",
#          "categoria":"",
#          "clasificacion":"",
#          "genero":"",
#          "idioma":""
#}

import mysql.connector
from mysql.connector import Error

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("Oprima cualquier tecla para continuar ...")  

def conectar():
  try:
      conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Alta de Peliculas ::. \n")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa el categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa el clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})

    ####### AGREGAR REGISTRO A LA BD
    try:
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) values (%s,%s,%s,%s,%s)"
      val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")
    except Error as e:
      print("Error al intentar insertar un registro en la BD")
    
def mostrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Consulta o Mostrar la pelicula ")
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("\n\tPeliculas en el sistema")
      print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificación":<15}{"Género":<15}{"Idioma":<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
    else:
      print("\t .:: No hay peliculas en el sistema ::.")

def buscarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Buscar una pelicula ::.\n")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("\n\tPeliculas en el sistema")
      print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificación":<15}{"Género":<15}{"Idioma":<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
    else:
      print("\t .:: La pelicula a buscar no se encuentra en el sistema ::.")

def borrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Borrar una pelicula ::.\n")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificación":<15}{"Género":<15}{"Idioma":<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
      resp=input(f"¿Deseas borrar la pelicula de {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
    else:
      print("\t .:: La pelicula a borrar no se encuentra en el sistema ::.")

def modificarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Modificar una pelicula ::.\n")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificación":<15}{"Género":<15}{"Idioma":<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
      resp=input(f"¿Deseas modificar la pelicula de {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
        pelicula["categoria"]=input("Ingresa el categoria: ").upper().strip()
        pelicula["clasificacion"]=input("Ingresa el clasificacion: ").upper().strip()
        pelicula["genero"]=input("Ingresa el genero: ").upper().strip()
        pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip()

        sql="update peliculas set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s where nombre=%s"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
        cursor.execute(sql,val)
        conexionBD.commit()
    else:
      print("\t .:: La pelicula a borrar no se encuentra en el sistema ::.")
  
