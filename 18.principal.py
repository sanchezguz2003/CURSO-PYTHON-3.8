import paquete_funciones
paquete_funciones.menu()
paquete_funciones.validando_opciones()

while True:
    decision=input("¿desea aser otra operacion? (S=si N=no):")
    paquete_funciones.menu()
    paquete_funciones.validando_opciones()
    if decision=="n" or decision=="N":
        break
print("gracias por usar la calculadora")
