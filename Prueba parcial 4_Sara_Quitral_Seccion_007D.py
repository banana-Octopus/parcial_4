# prueba parcial 4_Sara_Quitral_seccion_007D

lista_estudiantes=[]
estudiante={}
#funcion menu y opciones
def menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def opcion ():
    try:
        opc=int(input("ingrese una opcion "))
        if opc >=1 and opc <=6:
            return opc
        else:
            print("error")
            return 0

    except ValueError:
        print("ingrese una opcion valida")

#funcion validacion datos de estudiante
def validacion_nombre(nombre):
    nombre=input

    if nombre !="":
        print("nombre agregado correctamente")
        return True
    else:
        False

def validacion_edad(edad):
    if edad>0:
        print("edad agregada correctamente")
        return True
    else:
        False

def validacion_nota(nota):
    
    if nota >1.0 and nota <7.0:
        print("nota agregada correctamente")
        return True
    else:
        print("nota invalida")
        False

def agregar_estudiante(lista_estudiantes):
    
    nombre=input("ingrese el nombre del estudiante ")

    if not validacion_nombre(nombre):
        print("nombre invalido")
        return False
    
    try:
        edad=int(input("ingrese la edad del estudiante "))
        if not validacion_edad(edad):
            return
    except ValueError:
        return 
    
    try:
        nota=float(input("ingrese la nota del estudiante "))
        if not validacion_nota(nota):
            return
    except ValueError:
        return 
    
    estudiante={
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "estado": False
    }
    
    lista_estudiantes.append(estudiante)
    print("estudiante agregado exitosamente")

#funcion buscar estudiante

def buscar_estudiante(lista_estudiantes, estudiante_buscado):
    estudiante_buscado="estudiante".lower()
    for i in range(len(lista_estudiantes)):
        estudiante_actual=lista_estudiantes[i]["nombre"].lower()
        if estudiante_actual==estudiante_buscado:
            return i
    return -1

#eliminar estudiante
def eliminar_estudiante(lista_estudiantes):
    nombre=input("ingrese el nombre del estudiante a eliminar ")
    if posicion!=-1:
        lista_estudiantes.pop("estudiante")
        print("el estudiante a sido eliminado exitosamente")

    else:
        print(f"el estudiante",{nombre}, "no a sido registrado")

#funcion actulizar estado de estudiante
def actualizar_estado(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante ["nota"]>=4.0:
            estudiante["estado"]=True, "aprovado"
        else:
            estudiante["estado"]=False, "reprovado"

#funcion mostrar estudiantes
def mostrar_estudiantes(lista_estudiantes):
    actualizar_estado(lista_estudiantes)
    for estudiante in lista_estudiantes:
        mostrar_estudiantes(estudiante)
        print("=== LISTA DE ESTUDIANTES ===")
        print(estudiante=[])

#ejecutar programa
while True:
    menu()
    opc=opcion()
    
    if opc==1:
        agregar_estudiante(lista_estudiantes)

    elif opc==2:
        nombre=input("ingrese el nombre del estudiante a buscar ")
        posicion=buscar_estudiante(estudiante, nombre)
        if posicion !=-1:
            print({estudiante})
            actualizar_estado(estudiante)
            mostrar_estudiantes(estudiante[posicion])

    elif opc==3:
        eliminar_estudiante(estudiante)

    elif opc==4:
        actualizar_estado(estudiante)

    elif opc==5:
        mostrar_estudiantes(estudiante)

    elif opc==6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    else:
        print("intentalo denuevo")