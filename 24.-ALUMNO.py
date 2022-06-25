from persona import*
class ALUMNO(persona):
   def __init__(self,nombre,matricula):
       self.nombre=nombre
       self.matricula=matricula
   def comer(self):
       super().comer()
   def caminando(self):
       super().caminando()
   def promedio(self):
       return f"soy{self.nombre} y no tengo promedio aun"