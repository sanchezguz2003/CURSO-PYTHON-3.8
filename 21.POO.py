
class persona:

    nombre="diana"
    apellido="guzman"
    edad=18
    peso=45.5

    def __init__(self):
        print("iniciando clase")
    def caminar(self):
        print("estoy caminando")
    def comer(self):
        print("estoy comiendo")

persona=persona()
#print(persona.nombre)
#persona.caminar()
print(f"me llamo {persona.nombre} y {persona.caminar()}")