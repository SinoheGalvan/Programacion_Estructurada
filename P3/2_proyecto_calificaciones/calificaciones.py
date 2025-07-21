import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_calificaciones"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input(f"\t\t \U0001F552 Oprima cualquier tecla para continuar \U0001F552 ...")  

def menu_principal():
    print("\n\t\t..:::  Sistema de Gestión de Calificaciones :::...\n\t\t 1.- Agregar  \n\t\t 2.- Mostrar \n\t\t 3.- Calcular promedio \n\t\t 4.- SALIR ")
    opcion=input("\n\t\t Elige una opción (1-4): ").upper()

    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\t\t \U0001F4DD Agregar Calificaciones \U0001F4DD")
        nombre = input("\t\t \U0001F464 Nombre del alumno: ").upper().strip()
        calificaciones = []
        for i in range(1,4):
            continua = True
            while continua:
                try:
                    cal = float(input(f"\t\t\t Calificación {i} : "))
                    if cal >= 0 and cal < 11:
                        calificaciones.append(cal)
                        continua=False
                    else:
                        print("\t\t \u26A0 Ingresa un número valido \u26A0")
                except ValueError:
                    print("\t\t \u26A0 Ingresa un valor númerico \u26A0")
        lista.append([nombre]+calificaciones)
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO calificaciones (nombre, calificacion_1, calificacion_2, calificacion_3) VALUES (%s, %s, %s, %s)"
            valores = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])

            cursor.execute(sql, valores)
            conexion.commit()
            print("\t\t \u2705 Acción realizada con exíto \u2705")
        except Error as e:    
            print(f"Error al intentar insertar un registro en la BD {e}")

def mostrar_calificaciones(lista):
    borrarPantalla()
    conexion = conectar()
    if conexion!=None:
        print("\t\t \U0001F4C2 Mostrar Calificaciones \U0001F4C2")
        cursor=conexion.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(f"\t\t {"ID":<5}{'Nombre':<15}{'calif. 1':<10}{'Calif. 2':<10}{'Calif. 3':<10}")
            print(f"\t\t {'-'*40}")
            for fila in registros:
                print(f"\t\t{fila[0]:<5}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print(f"\t\t {'-'*40}")
            cuantos=len(registros)
            print(f"\t\t \U0001F464 Son {cuantos} alumnos")
        else:
            print("\t\t \U0001F4DB No hay calificaciones registradas en el sistema \U0001F4DB")

def calcular_promedios(lista):
    borrarPantalla()
    conexion = conectar()
    if conexion!=None:
        print("\t\t \u1F4C .:: PROMEDIOS ::.")
        cursor=conexion.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(f"\t\t{'Alumno':<15}{'Promedio:':<10}")
            print(f"\t\t{'-'*30}")
            promedio_grupal=0
            for fila in registros:
                nombre=fila[1]
                promedio=sum(fila[2:])/3           
                print(f"\t\t{nombre:<15}{promedio:.2f}")
                promedio_grupal+=promedio
            print(f"\t\t{'-'*30}")
            promedio_grupal=promedio_grupal/len(registros)
            print(f"\t\t El promedio grupal es: {promedio_grupal}")
        else:
            print("\t\t \u274C No hay calificaciones registradas en el sistema \u274C")

# def calcular_promedios2(lista):
#     borrarPantalla()
#     print("\t\t .:: PROMEDIOS ::.")
#     if len(lista)>0:
#         print(f"{'Nombre':<15}{'Promedio:':<10}")
#         print(f"{'-'*30}")
#         for fila in lista:
#             nombre=fila[0]
#             i=1
#             suma=0
#             promedio=0
#             promedio_grupal=0
#             while i<=3:
#                 suma+=fila[i]
#                 i+=1
#             promedio=suma/3
#             print(f"{nombre:<15}{promedio:.2f}")
#             promedio_grupal+=promedio
#         print(f"{'-'*30}")
#         promedio_grupal=promedio_grupal/len(lista)
#         print(f"El promedio grupal es: {promedio_grupal}")
#     else:
#         print("\t\t \u274C No hay calificaciones registradas en el sistema \u274C")