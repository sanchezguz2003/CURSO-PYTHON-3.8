

lista_alumnos_ISIC=[
                    ["Miguel Angel","Olivera Ortega","miguel@gmail.com"],
                    ["Marina","Toribio Salgado","marina@gmail.com"],
                    ["Victor","Mateos Francisco","victor@gmail.com"],
                    ["Gabriel","Garcia Dolores","gabriel@gmail.com"],
]
print(lista_alumnos_ISIC)

#un solo registro
#print(lista_alumnos_ISIC[1])
#mostrar una lista determinada
#print(lista_alumnos_ISIC[1])
#mostrar un registro
#print(lista_alumnos_ISIC[3][2])

#mostrar nombres
#for nombres in lista_alumnos_ISIC:
 #   print(nombres[0])
 #   print(nombres[1])

for alumnos in lista_alumnos_ISIC:
    for elementos in alumnos:
        if alumnos.index(elementos)==0:
            print(f"nombre:{elementos}")
        elif alumnos.index(elementos)==1:
            print(f"apellidos:{elementos}")
        elif alumnos.index(elementos)==2:
            print(f"correo:{elementos}")