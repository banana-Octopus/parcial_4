#evaluacion formativa 4_2

#menu
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("=====================================")

#opcion

def leer_opcion():
    try:
        opcion=int(input("seleccione una opcion: "))
        if opcion>=1 and opcion<=6:
            return opcion
        else:
            print("error:debe ingresar una opcion del 1 al 6")
            return 0
    except ValueError:
        print("igresa un numero entero")

#validacion nombre

def validacion_nombre(nombre):
    if nombre.strip() !="":
        return True

    else:
        return False

#validacio de edad

def validacion_edad(edad):
    if edad >0:
        return True

    else:
        return False
    

#validacion de temperatura
def validacion_temperatura(temperatura):
    if temperatura >=35.0:
        return True
    else:
        False


def validacion_paciente(lista_pacientes):
    print()
    print("agregar paciente")

    nombre=input("ingrese el nombre del paciente ")+

    if not validacion_nombre(nombre):
        print("nombre invalido")
        return
    
    try:
        edad=int(input("ingrese la edad del paciente"))
        if not validacion_edad(edad):
            print("error")
            return
    except ValueError:
        print("ingrese una edad invalida")
        return
    
    try:
        temperatura=float(input("ingrese la temperatura del paciente "))

        if not validacion_temperatura(temperatura):
            print("error")
    except ValueError:
        print("ingrese una temperatura valida")


    paciente={
        "nombre":nombre,
        "edad":edad,
        "temperatura":temperatura,
        "atendido":False
    }
    lista_pacientes.append(paciente)
    print("paciente agregadio correctamente")
