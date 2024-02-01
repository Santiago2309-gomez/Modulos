import validate as val
from module.validate import menuNoValid
from os import system

def save ():
    return "Sucessfully"

def edit():
    return "Edit to trainer"

def search():
    return"The trainer is available"

def delete():
    return "Trainer deleted"

def menu():
    print("CRUD del trainer")
    print("\t1. Guardar trainer")
    print("\t2. Buscar trainer")
    print("\t3. Actualizar trainer")
    print("\t4. Eliminar trainer")
    print("\t0. Atras")
    opc = int(input())
    match(opc):
        case 1:
            system("clear")
        case 0:
            #print("Salir del menú camper")
            system("clear")
        case _:
             menuNoValid(opc)