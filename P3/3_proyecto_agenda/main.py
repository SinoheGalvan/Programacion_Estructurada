import agenda

def main():

    agenda_contactos = {}

    opcion=True
    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()
    
        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contactos(agenda_contactos)
                agenda.esperarTecla()  
            case "3":
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()     
            case "6":
                opcion=False
                agenda.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion=True 
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()