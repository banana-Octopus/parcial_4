#clase 15-6

#sistema de vehiculos

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("\n1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("\n=====================================")

#funcion para leer

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
        
#valiudacion de modelo

def validacion_modelo(modelo):
    if modelo.strip() !="":
        return True

    else:
        return False

#validacion del año
def validacion_año(año):
    if año > 1900:
        return True
    else:
        return False
    
#validacion precio

def validacion_precio(precio):
    if precio >0:
        return True
    else:
        return False
    
#funcion vehiculo

def agregar_vehiculo(lista_vehiculos):
    print()
    print("agregar vehiculo")

    modelo = input("agrega el modelo del vehiculo: ")

    if not validacion_modelo(modelo):
        print("error, modelo invalido bla bla bliblu")
        return 
    
    try:
        año = int(input("ingrese el año del auto": ))
        if not validacion_año(año):
            print("error, sigue")
            return 
    except ValueError:
        print("error:ingrese un año valido")
        return
    
    try:
        precio = float(input("ingrese el valor del vehiculo: "))

        if not validacion_precio(precio):
            print("error, el precio debe ser mayor a cero")
            return
    except ValueError:
        print("error, el precio debe ser un numero decimal")
        return
    
    vehiculo = {
        "modelo": modelo.strip(),
        "año": año,
        "precio": precio,
        "disponible": False
    }
    
    lista_vehiculos.append(vehiculo)    

    print("vehiculo agregado correctamente")
