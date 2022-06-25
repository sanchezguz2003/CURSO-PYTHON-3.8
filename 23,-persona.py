class persona:
    def __init__(self,nombre,apellidos,edad):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
    def comer(self):
        print(self.nombre,"esta comiendo")

    def caminando(self):
        print(self.nombre,"esta caminando")