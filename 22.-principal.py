

from ALUMNO import*
#creando objetos
persona1=persona("nicolas","guzman",30)
print("me llamo",persona1.nombre)
print("mis apellidos",persona1.apellidos)
print("y tengo",persona1.edad,"años")
persona1.comer()
persona1.caminando()

#llamando alumno
alumno1=ALUMNO("miguel","S0202201")
print(alumno1.promedio())
print(alumno1.comer())

mi_archivo=open("nota fundamentos.txt","w")
try:
    mi_archivo.write(f"esta es una persona {alumno1.nombre}\n")
    mi_archivo.write(f"otra persona {persona1.nombre}")
finally:
    mi_archivo.close()
