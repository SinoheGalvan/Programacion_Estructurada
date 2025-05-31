"""
Crear un programa que calcule e imprima las tablas de multiplicar del 2
Requisitos

V1

"""
#V2



def multi_While(num):
    i=1
    rsp = ""
    while(i<=10):
        rsp = rsp + (f"{num} x {i} = {num*i}\n")
        i+=1
    return rsp


def multi_For(num):
    rsp=""
    for i in range (1,11):
        rsp = rsp + (f"{num} x {i} = {num*i}\n")
    return rsp

num = int(input("Ingrese el numero de la tabla de multiplicar: "))
tablas = multi_For(num)
print(tablas)
