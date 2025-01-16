'''
Principio de la segregación de la interfaz: No forzare al cliente a 
-depender de interfaces que no utilizamos
'''

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass

class Comer(ABC):
    @abstractclassmethod
    def comer(self):
        pass
class Dormir(ABC):
    @abstractclassmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comer, Dormir):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")

class Robot(Trabajador):
   
    def trabajar(self):
        print("El robot está trabajando")
        
robot1 = Robot()
robot1.trabajar()

humano1 = Humano()
humano1.comer()