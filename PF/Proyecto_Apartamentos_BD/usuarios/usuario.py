from conexionBD import *
import hashlib

def registrar(correo,password):
    try:
        contrasena = hash_password(password)
        sql = "insert into usuarios (correo,contrasena) values(%s,%s)"
        val = (correo,contrasena)
        cursor1, conexion1 = conectarBD()
        if cursor1 == None:
            print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
            input("\n🔄 Ingrese enter para continuar")
            return 
        cursor1.execute(sql,val)
        desconectarBD(conexion1)
        return True
    except:
        return False
        
def iniciar_sesion(email,contrasena):
    try:
        cursor1, conexion1 = conectarBD()
        if cursor1 == None:
            print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
            input("\n🔄 Ingrese enter para continuar")
            return 
        password = hash_password(contrasena)
        cursor1.execute(f"select * from usuarios where correo = '{email}' and contrasena = '{password}'")
        registros = cursor1.fetchone()
        if registros == None:
            return False
        else: 
            return True
    except:
        return None
    
def hash_password(contrasena):
    return hashlib.sha3_256(contrasena.encode()).hexdigest()