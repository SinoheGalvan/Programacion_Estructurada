#1er utilizar los modulos
import modulos

modulos.borrarPantalla
print(modulos.saludar("Jose Sinohe Galvan Rios"))

#2da forma de utilizar modulos
from modulos import saludar, borrarPantalla

borrarPantalla
print(saludar("El santo"))

nombre=input("Ingrese el nombre del contacto: ")
telefono=input("Ingresa su número de telefono con clave lada: ")
nom,tel=modulos.solicitar_4(nombre,telefono)
print(f"\tNombre completo: {nom} \n\tTelefono: {tel}")



