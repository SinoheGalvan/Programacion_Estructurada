
def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input(f"\t\t \U0001F552 Oprima cualquier tecla para continuar \U0001F552 ...")  

def menu_principal():
    print("\n\t 📆..:::  Sistema de Gestión de Agenda de Contactos :::...📆\n\t\t 1️⃣ Agregar contacto  \n\t\t 2️⃣ Mostrar todos los contactos \n\t\t 3️⃣ Buscar contacto por nombre \n\t\t 4️⃣ Modificar contacto \n\t\t 5️⃣ Eliminar contacto \n\t\t 6️⃣ SALIR ")
    opcion=input("\n\t\t Elige una opción (1-6): ").upper()

    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.:: Agregar Contactos ::.")
    nombre = input("\n\t\t Nombre del Contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t Contacto ya existe ")
    else:
        tel = input("\t\t Teléfono: ").strip()
        email = input("\t\t E-mail: ").lower().strip()
        agenda[nombre]= [tel,email] #agregar el atributo "nombre" al dict con los valores de telefono y email en una lista
        print("\n\t\t .:: Acción realizada con éxito ::.")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t .:: Mostrar Contactos ::.")
    if not agenda:
        print("\n\t\t No existen contactos en la Agenda ....")
    else:
        for nombre,datos in agenda.items():
            print(f"\n\t{'Nombre:'+nombre}\n\t{'Teléfono: '+datos[0]}\n\t{'Email:'+datos[1]}")

def buscar_contacto(agenda):
    borrarPantalla()
    encontrado = False
    print("\n\t\t .:: Busqueda de contactos por nombre ::.")
    nombre_buscar = input("\n\t\t Nombre del contacto a buscar: ").upper().strip()
    for nombre,datos in agenda.items():
        if nombre == nombre_buscar:
            print(f"\n\t{'Nombre:'+nombre}\n\t{'Teléfono: '+datos[0]}\n\t{'Email:'+datos[1]}")
            encontrado = True
    if not encontrado:
        print("\n\t\t Este contacto no existe")

def modificar_contacto(agenda):
    borrarPantalla()
    encontrado = False
    print("\n\t\t .:: Busqueda de contactos por nombre ::.")
    nombre_buscar = input("\n\t\t Nombre del contacto a modificar: ").upper().strip()
    for nombre,datos in agenda.items():
        if nombre == nombre_buscar:
            print(f"\n\t{'Nombre:'+nombre}\n\t{'Teléfono: '+datos[0]}\n\t{'Email:'+datos[1]}")
            encontrado = True

            opcion = input("\n\t¿Desea editar este contacto? (S/N): ").upper().strip()
            if opcion == "S":
                print("\n\t1. Cambiar nombre")
                print("\t2. Cambiar teléfono")
                print("\t3. Cambiar email")
                print("\t4. Cambiar todo")
                opcion_editar = input("\n\tSeleccione una opción: ")
                
                if opcion_editar == "1":
                    nuevo_nombre = input("\n\tNuevo nombre: ").upper().strip()
                    agenda[nuevo_nombre] = agenda.pop(nombre)  # Cambia la clave (nombre)
                    print("\n\t\t .:: Acción realizada con éxito ::.")
                elif opcion_editar == "2":
                    nuevo_tel = input("\n\tNuevo teléfono: ").strip()
                    agenda[nombre][0] = nuevo_tel
                    print("\n\t\t .:: Acción realizada con éxito ::.")
                
                elif opcion_editar == "3":
                    nuevo_email = input("\n\tNuevo email: ").strip()
                    agenda[nombre][1] = nuevo_email
                    print("\n\t\t .:: Acción realizada con éxito ::.")
                else:
                    print("\n\tOpción no válida")
    if not encontrado:
        print("\n\t\t Este contacto no existe")

def eliminar_contacto(agenda):
    encontrado = False
    print("\n\t\t .:: Busqueda de contactos por nombre ::.")
    nombre_buscar = input("\n\t\t Nombre del contacto a buscar: ").upper().strip()
    for nombre,datos in agenda.items():
        if nombre == nombre_buscar:
            print(f"\n\t{'Nombre:'+nombre}\n\t{'Teléfono: '+datos[0]}\n\t{'Email:'+datos[1]}")
            encontrado = True

            opcion = input("\n\t¿Desea eliminar este contacto? (S/N): ").upper().strip()
            if opcion == "S":
                agenda.pop(nombre)
                print("\n\t\t .:: Acción realizada con éxito ::.")
    if not encontrado:
        print("\n\t\t Este contacto no existe")