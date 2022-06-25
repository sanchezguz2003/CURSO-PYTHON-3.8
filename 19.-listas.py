#lista_nombres=["Diana",23,12.9,True]
#lista1=list["hola",23,2.9]
#imprimir lista
#print(lista_nombres)
#acceder a una pocision

lista_nombres=["Diana","bruno","victor","gabriel"]
lista_numeros=[2,8,12,1,90]
print(lista_numeros)
print(lista_nombres)

#tamaño lista
print(len(lista_nombres))
#acceder a una pocision
print(lista_nombres[1])

#imprimir rango determinado
print(lista_nombres[2][3])

#agregar un elemento
lista_nombres.insert(0,"cira")
print(lista_nombres)

#iterar
for elementos in lista_nombres:
    print(elementos)

#agregar
lista_nombres.append("Miguel")
print(lista_nombres)

#quitar un elemento
lista_nombres.remove("bruno")
print(lista_nombres)

#eliminar el ultimo elemento de la lista
lista_nombres.pop()
print(lista_nombres)

#limpiar la lista
lista_nombres.clear()
print(lista_nombres)

#alimpiar lista
#del lista_nombres
#print(lista_nombres)

#ordenar
lista_numeros.sort()
print(lista_numeros)


