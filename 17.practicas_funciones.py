
def menu():
    print("1 para suma")
    print("2 para resta")
    print("3 para multiplicacion")
    print("4 para division")

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

def validando_opciones():
    opcion=int(input("anota opcion(1=suma,2=resta,3=mult.,4=div.,:"))
    numero1=int(input("anota un numero: "))
    numero2=int(input("anota otro numero"))

    if opcion==1:
        print(suma(numero1,numero2))
    elif opcion==2:
        print(resta(numero1,numero2))
    elif opcion==3:
        print(multiplicacion(numero1,numero2))
    elif opcion==4:
        print(division(numero1,numero2))