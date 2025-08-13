from funciones import *
from conexionBD import *

def agregarRegistro():
    borrarPantalla()
    print("\n\t..::📝 Agregar Registro 📝::..")
    cursor1, conexion1= conectarBD()
    if cursor1 == None:
        print(f"Conexion con la base de datos fallida\nError {conexion1}")
        input("\nIngrese enter para continuar")
        return 
    nuevo = []
    items = ["id","No. Apartamento","Direccion","Descripcion"]
    for i in range(1,len(items)):
        nuevo.append(input(f"\t💾Ingrese {items[i]} del apartamento: \n\t->").upper().strip())

    if cursor1 == None:
        print(f"❌ Conexión con la base de datos fallida\n Error {conexion1}")
        input("\n🔄 Presione enter para continuar")
        return 
    sql="insert into apartamentos values (null,%s,%s,'NO',%s)"
    cursor1.execute(sql, nuevo)
    desconectarBD(conexion1)
    print("\t\tLa operación se realizó con exito")
    esperarTecla()

def modificarRegistro():
    borrarPantalla()
    print("\n\t .::🔄 Modificar Registros 🔄::. \n")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"Conexion con la base de datos fallida\nError {conexion1}")
        input("\nIngrese enter para continuar")
        return 
    mostrarTodo()
   

    id_cambiar=comprobar(input("Introduce el ID del registro a modificar: "))
    if id_cambiar == None:
        esperarTecla()  
        return
    items = ["id","direccion","descripcion"]
    cursor1.execute(f"select * from apartamentos where id = {id_cambiar}")
    registros = cursor1.fetchall()
    if registros == []:
        print("\t\t No se encontró ningún registro")
    else:
        mostrar = [["id","Apartamento","Direccion","Ocupado","Descripcion"]]
        mostrar.extend(registros)
        print(f"{tabulate(mostrar, tablefmt="grid", colalign = ("center",) * 5)}\n")
        for i in range(1,len(items)):
            rsp = input(f"\t\t📝 Desea cambiar el {items[i]} del apartamento? \n\t\t->").upper().strip()
            if rsp == "SI":
                nuevo = input("\t\tIngrese el nuevo valor\n\t\t->").upper().strip()
                cursor1.execute(f"update apartamentos set {items[i]}='{nuevo}' where id={id_cambiar}")
                print("\t\t..::OPERACIÓN EXITOSA::.. ")
                    
    desconectarBD(conexion1)
    esperarTecla()  

def mostrarRegistro():
    borrarPantalla()
    print(f"{'\t'*4}..::🔍 Mostrar Registros 🔍::..")
    mostrarTodo()
    esperarTecla()

def buscarRegistro():
    borrarPantalla()
    print(f"{'\t'*3}..::🔍 Buscar Registros 🔍::..")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"Conexion con la base de datos fallida\nError {conexion1}")
        input("\nIngrese enter para continuar")
        return 
    campo = input("\t\tIngrese el campo por el cual desea buscar uno o más registros\n\t\t(Campos: id,apartamento,direccion,ocupado,descripcion): \n\t\t->").upper().strip()
    registro = input("\t\tIngrese el valor para buscar\n\t\t->").upper().strip()
    try:
        cursor1.execute(f"select * from apartamentos where {campo} = '{registro}'")
        registro = cursor1.fetchall()
        if registro == []:
            print("\t\tNo se encontró ningun valor coincidente")
        else:
            borrarPantalla()
            mostrar = [["id","No. Apartamento","Direccion","Ocupado","Descripcion"]]
            mostrar.extend(registro)
            print(f"{tabulate(mostrar, tablefmt="grid", colalign = ("center",) * 5)}\n")
    except:
        print("\t\tEl campo ingresado no se encuentra, verifiquelo")

    desconectarBD(conexion1)
    esperarTecla()

def borrarRegistro():
    borrarPantalla()

    print("\n\t .::📛 Borrar Registros 📛::. \n")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"Conexion con la base de datos fallida\nError {conexion1}")
        input("\nIngrese enter para continuar")
        return 
    mostrarTodo()
    id_cambiar=comprobar(input("Introduce el ID del registro que desea borrar: "))
    if id_cambiar == None:
        esperarTecla()  
        print("\t\t❌ Operación cancelada, no se eliminó ningún registro 🚫")
        return
    cursor1.execute(f"select * from apartamentos where id = {id_cambiar}")
    registro = cursor1.fetchall()
    mostrar = [["id","No. Apartamento","Direccion","Ocupado","Descripcion"]]
    mostrar.extend(registro)
    print(f"{tabulate(mostrar, tablefmt="grid", colalign = ("center",) * 5)}\n")
    
    rsp = input("\n\t\tADVERTENCIA: Si hay un cliente ocupando este apartamento también se borrara su registro"
                "\n\t\tEstá seguro de que desea borrar este registro?(SI/NO): ").upper().strip()
    if rsp == "SI":
        apt = mostrar[1][1]
        cursor1.execute(f"DELETE FROM clientes where apartamento={apt}")
        cursor1.execute(f"DELETE FROM apartamentos WHERE id = {id_cambiar}")
        print("\t\t..::OPERACIÓN EXITOSA::.. ")
    else: 
        print("\n\t\tNo se eliminó ningun registro")
                    
    
    desconectarBD(conexion1)
    esperarTecla()

def mostrarTodo():
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"Conexion con la base de datos fallida\nError {conexion1}")
        input("\nIngrese enter para continuar")
        return 
    cursor1.execute("select * from apartamentos")
    registros = cursor1.fetchall()
    mostrar = [["id","No. Apartamento","Direccion","Ocupado","Descripcion"]]
    mostrar.extend(registros)
    print(f"{tabulate(mostrar, tablefmt="grid", colalign = ("center",) * 5)}\n")
    desconectarBD(conexion1)
    
def comprobar(id):
    try:
        id = int(id)
        return id
    except:
        print("Ingrese solo numeros")
        return None
    