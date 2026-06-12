#clase 3_6
#solicitar el nombre
nombre=input("por favor, dime tu nombre")
#lista
notas=[]
#notas
for i in range(3):
    nota=float(input(f"ingrese la nota{i+1}: "))
    notas.append(nota)

    suma=0

for nota in notas:
    suma = suma+nota

promedio =suma/len(notas)

estudiante={
    "nombre":nombre,
    "notas":notas,
    "promedio": promedio,
}

#mostrar
print("\n resumen")
print("-------------------------------")
print("nombre", estudiante["nombre"])
print("nota", estudiante["notas"])
print("nota", estudiante["promedio"])

""""
notas=[5.5,6.1,9]
print(min(notas))
"""