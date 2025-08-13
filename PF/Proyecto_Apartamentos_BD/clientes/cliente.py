from funciones import *
from conexionBD import *

def agregarRegistro():
    borrarPantalla()
    print("\n\t..::📝 Agregar Registro 📝::..")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
        input("\n🔄 Ingrese enter para continuar")
        return 
    cursor1.execute("select * from apartamentos where ocupado='NO'") 
    registros = cursor1.fetchall()
    if registros == []:
        print("\n\t\t...🚫 No hay apartamentos disponibles...")
    else:        
        mostrar = [["id","No. Apartamento","Direccion","Ocupado","Descripcion"]]
        mostrar.extend(registros)
        print("\n\t🏢 Los apartamentos disponibles son los siguientes: ")
        print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 5)}\n")
        nuevo = []
        items = ["ID","Nombre","Teléfono", "Num. de Apartamento","Monto a pagar","Dia de pago","Estatus" ]
        for i in range(1, len(items)):
            if i == 3:
                valido = True
                while valido:
                    apt = comprobar(input(f"\t💾 Ingrese el {items[i]} de la persona: \n\t-> "))
                    if apt != None:
                        cursor1.execute(f"select apartamento from apartamentos where ocupado='NO' and apartamento = {apt}")
                        registros = cursor1.fetchall()
                        if registros == []:
                            print("\n\t⚠️ Ingrese un numero de apartamento disponible")
                        else:
                            nuevo.append(apt)
                            cursor1.execute(f"update apartamentos set ocupado = 'SI' where apartamento = {apt}")
                            valido = False
            else:
                nuevo.append(input(f"\t💾 Ingrese el {items[i]} de la persona: \n\t-> ").upper().strip())
        if cursor1 == None:
            print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
            input("\n🔄 Ingrese enter para continuar")
            return 
        sql = "insert into clientes(Nombre, Telefono, Apartamento, Monto, Dia, Estatus) values (%s,%s,%s,%s,%s,%s)"
        cursor1.execute(sql, nuevo)
        print("\t\t✅ La operación se realizó con exito")
    desconectarBD(conexion1)
    esperarTecla()

def modificarRegistro():
    borrarPantalla()
    print("\n\t .::🔄 Modificar Registros 🔄::. \n")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
        input("\n🔄 Ingrese enter para continuar")
        return 
    mostrarTodo()
    id_cambiar = comprobar(input("🆔 Introduce el ID del registro a modificar: "))
    if id_cambiar == None:
        esperarTecla()  
        return
    items = ["ID","Nombre","Telefono", "Apartamento","Monto","Dia","Estatus" ]
    cursor1.execute(f"select * from clientes where ID = {id_cambiar}")
    registros = cursor1.fetchall()
    if registros == []:
        print("\t\t❌ No se encontró ningún registro")
    else:
        mostrar = [["ID","Nombre","Teléfono", "Num. de Apartamento","Monto a pagar","Dia de pago","Estatus" ]]
        mostrar.extend(registros)
        print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 7)}\n")
        old_apt = mostrar[1][3]
        for i in range(1, len(items)):
            rsp = input(f"\t\t📝 Desea cambiar el {items[i]} de la persona? \n\t\t-> ").upper().strip()
            if rsp == "SI":
                if i == 3:
                    cursor1.execute("select * from apartamentos where ocupado='NO'")
                    registros = cursor1.fetchall()
                    if registros == []:
                        print("\n\t\t...🚫 No hay apartamentos disponibles...")
                    else:
                        mostrar = [["id","No. Apartamento","Direccion","Ocupado","Descripcion"]]
                        mostrar.extend(registros)
                        print("\n\t🏢 Los apartamentos disponibles son los siguientes: ")
                        print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 5)}\n")
                        valido = True
                        while valido:
                            apt = comprobar(input(f"\t💾 Ingrese el numero del nuevo apartamento de la persona: \n\t-> "))
                            if apt != None:
                                cursor1.execute(f"select * from apartamentos where ocupado='NO' and apartamento = {apt}")
                                registros = cursor1.fetchall()
                                if registros == []:
                                    print("\n\t⚠️ Ingrese un numero de apartamento disponible")
                                else:
                                        cursor1.execute(f"update clientes set apartamento = '{apt}' where ID={id_cambiar}")
                                        print("\t\t✅ OPERACIÓN EXITOSA ")
                                        cursor1.execute(f"update apartamentos set ocupado = 'SI' where apartamento = {apt}")
                                        cursor1.execute(f"update apartamentos set ocupado = 'NO' where apartamento = {old_apt}")
                                        valido = False
                else:
                    nuevo = input("\t\t✏️ Ingrese el nuevo valor\n\t\t-> ").upper().strip()
                    cursor1.execute(f"update clientes set {items[i]}='{nuevo}' where ID={id_cambiar}")
                    print("\t\t✅ OPERACIÓN EXITOSA ")

    desconectarBD(conexion1)
    esperarTecla()  

def mostrarRegistro():
    borrarPantalla()
    print(f"{'\t'*4}..::🔍 Mostrar Registros 🔍::..")
    mostrarTodo()
    esperarTecla()

def mostrarTodo():
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
        input("\n🔄 Ingrese enter para continuar")
        return 
    cursor1.execute("select * from clientes")
    registros = cursor1.fetchall()
    mostrar = [["ID","Nombre","Teléfono", "Num. de Apartamento","Monto a pagar","Dia de pago","Estatus" ]]
    mostrar.extend(registros)
    print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 7)}\n")
    desconectarBD(conexion1)

def buscarRegistro():
    borrarPantalla()
    print(f"{'\t'*3}..::🔍 Buscar Registros 🔍::..")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
        input("\n🔄 Ingrese enter para continuar")
        return 
    campo = input("\t\t🔎 Ingrese el campo por el cual desea buscar uno o más registros\n\t\t(Campos: id, nombre, telefono, apartamento, monto, dia, estatus.): \n\t\t-> ").upper().strip()
    registro = input("\t\t🔎 Ingrese el valor para buscar\n\t\t-> ").upper().strip()
    try:
        cursor1.execute(f"select * from clientes where {campo} = '{registro}'")
        registro = cursor1.fetchall()
        if registro == []:
            print("\t\t❌ No se encontró ningun valor coincidente")
        else:
            mostrar = [["ID","Nombre","Teléfono", "Num. de Apartamento","Monto a pagar","Dia de pago","Estatus" ]]
            mostrar.extend(registro)
            print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 7)}\n")
    except:
        print("\t\t⚠️ El campo ingresado no se encuentra, verifiquelo")
    desconectarBD(conexion1)
    esperarTecla()

def borrarRegistro():
    borrarPantalla()
    print("\n\t .::📛 Borrar Registros 📛::. \n")
    cursor1, conexion1 = conectarBD()
    if cursor1 == None:
        print(f"❌ Conexion con la base de datos fallida\nError {conexion1}")
        input("\n🔄 Ingrese enter para continuar")
        return 
    mostrarTodo()
    id_cambiar = comprobar(input("🆔 Introduce el ID del registro que desea borrar: 🗑️\n\t-> "))
    if id_cambiar == None:
        esperarTecla()  
        return
    cursor1.execute(f"select * from clientes where id = {id_cambiar}")
    registro = cursor1.fetchall()
    if registro == []:
        print("\t\t❌ No se encontró ningún registro")
    else:
        mostrar = [["ID","Nombre","Teléfono", "Num. de Apartamento","Monto a pagar","Dia de pago","Estatus" ]]
        mostrar.extend(registro)
        apt = mostrar[1][3]
        print(f"{tabulate(mostrar, tablefmt='grid', colalign = ('center',) * 7)}\n")
        rsp = input("\n\t\t⚠️ Está seguro de que desea borrar este registro?(SI/NO): ").upper().strip()
        if rsp == "SI":
            cursor1.execute(f"DELETE FROM clientes WHERE ID = {id_cambiar}")
            cursor1.execute(f"update apartamentos set ocupado = 'NO' where apartamento = {apt}")
            print("\t\t✅ OPERACIÓN EXITOSA ")
        else: 
            print("\n\t\t❌ No se eliminó ningun registro")
    desconectarBD(conexion1)
    esperarTecla()  

def comprobar(id):
    try:
        id = int(id)
        return id
    except:
        print("⚠️ Ingrese solo numeros")
        return None
