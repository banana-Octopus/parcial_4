#evaluacion formativa 4

lista_vehiculos=[]

def vehiculo():
    print("========== MENÚ PRINCIPAL ==========")
    print("\n1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("\n=====================================")


def opcion():
    opc=int(input("elija una opcion "))
    return opc

while True:
    vehiculo()
    opc=opcion()
    auto={}
    if opc==1:
        modelo=input("ingrese modelo del vehiculo ").strip()
        if len(modelo)==0:
            print("no puede dejar vacio el espacio del nombre del modelo")
        elif modelo==" ":
            print("no dejes espacios en blanco")
        else:
            auto["modelo"]=modelo

        año=int(input("ingrese el año del vehiculo "))
        if año<=1900:
            print("el año del auto debe ser mayor a 1900")
        else:
            auto["año"]=año

        precio=int(input("ingrese el precio del vehiculo(sin puntos) "))
        if precio<=0:
            print("el precio debe ser mayor a cero")
        else:
            auto["precio"]=precio
        lista_vehiculos.append(auto)

    if opc==2:
        def buscar_auto():
            if len(lista_vehiculos)==0:
                print("no hay autos registrados")
            else:
                buscar=input("ingrese el modelo del vehiculo ")
                if buscar==auto:
                    for auto in lista_vehiculos:
                        return auto
                else:
                    print("ingrese un auto registrado")
        buscar_auto()
    if opc==3:
        buscar_auto()[lista_vehiculos]
        if buscar_auto==0:
            print("no hay autos registrados")
        else:
            print(lista_vehiculos)
            eliminar=input("¿que auto desea eliminar? ")
            if eliminar==auto:
                lista_vehiculos.remove(auto)

    if opc==4:
        def autos_disp():
            if auto["año"]>=2020:
                for auto in lista_vehiculos:
                    lista_vehiculos.remove(auto)
                    True
                return(lista_vehiculos)
            else:
                "año"<=2020
                False
                

        autos_disp()

    if opc==5:
        if autos_disp(True):
            print("====LISTA DE VEHICULOS===")
            print([lista_vehiculos])
        else:
            print("no hay autos disponibles")

    if opc==6:
        break
        



    