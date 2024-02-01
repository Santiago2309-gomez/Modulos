#Toda la informacion del camper 
#Funciones lo que hace es retornar un mensaje
import json
from os import system
from .data import camper, generos
from .validate import menuNoValid
def save ():
    info = {
        "Nombre": input ("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido: "),
        "Edad": int(input("Ingrese la edad: ")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    with open("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return f"Sucessfully Camper"

def edit():
    bandera=True
    while(bandera):
        system("clear")
        print("""
        ************************************************
                   *ACTUALIZACIÓN CAMPER*
        ************************************************
""")
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar"))
    print(f"""
___________________________________________________
#el .get significa obtener del diccionar un parametro en especifico                    
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido {camper[codigo].get('Apellido')}  
Edad {camper[codigo].get('Edad')}
Genero: {camper[codigo].get('Genero')}
____________________________________________________
""")

    print("¿Este es el camper que deseas actualizar?")
    print("1.Si")
    print("2.No")
    print("3.Salir")
    opc = int (input())
    if (opc == 1):
        info = {
            "Nombre": input("Ingrese el nombre del camper\n"),
            "Apellido": input ("Ingrese el apellido del camper\n"),
            "Edad": int(input("Ingrese la edad del camper\n")),
            "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))    
        }
        camper[codigo] = info
        with open("module/storage/camper.json","w") as f:
            data= json.dumps(camper, indent=4)
            f.write(data)
            f.close()
        bandera == False
    elif (opc == 3):
        bandera = False 
    return "Edit to camper"

def search():
        system("clear")
        print(f"""       
*************************       
    *lista Camper*
*************************
""")
for i, val in enumerate(camper):
        print(f"""
___________________________________________________
Codigo:{i}
Nombre: {val.get('Nombre')}
Apellido {val.get('Apellido')}  
Edad {val.get('Edad')}
Genero: {val.get('Genero')}
____________________________________________________
    """)
   return "The camper is avaliable"
    

def delete():
    bandera = True
    while (bandera):
        system("clear")
        print(f"""       
***************************       
    *Eliminación Camper*
***************************
""")
    codigo = int(input("Ingrese el codigo del camper que desea eliminar"))
    print(f"""
___________________________________________________
Codigo:{codigo}
Nombre: {camper[Codigo].get('Nombre')}
Apellido {camper[Codigo].get('Apellido')}  
Edad {camper[Codigo].get('Edad')}
Genero: {camper[Codigo].get('Genero')}
____________________________________________________
    """)
    print("¿Este es el codigo que deseas eliminar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")
    opc = int(input())
    if (opc == 1):
         camper.pop(codigo)
         with open("module/storage/camper.json", "w") as f:
              data = json.dumps(camper, ident=4)
              f.write(data)
              f.close()
         bandera = False
    elif (opc == 2):
         print("_________________________")
         print("¿Que desea hacer?")
         print("1. Volver al menú")
         print("2. Eliminar camper")
         opc2 = int(input())
         if (opc2 == 1):
              system("clear")
              menu()
         elif(opc2 == 2):
            system("clear")
            camper.pop(codigo)
            with open("module/storage/camper.json", "w") as f:
                 data = json.dumps(camper, ident=4)
                 f.write(data)
                 f.close()
    elif(opc == 3):
         bandera = False
    return "Camper deleted"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Eliminar camper")
        print("\t0. Atras")
        opc = int(input())
    match(opc):
        case 1: save()
        case 2: search()
        case 3: edit()
        case 4: delete()
        case 0:
            #print("Salir del menú camper")
            system("clear")
            bandera = False
        case _:
             menuNoValid(opc)