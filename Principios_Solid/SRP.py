#Principio de resposabilidad unica: Cada clase debe hacer una unica tarea

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 25

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -=cantidad

class Auto ():
    def __init__(self, tanque):
         self.posicion = 0
         self.tanque = tanque

    def mover (self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("El auto se ha movido exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

tanque = TanqueDeCombustible()
auto1= Auto(tanque)
print(auto1.obtener_posicion())
print(auto1.mover(10))
print(auto1.obtener_posicion())
print(auto1.mover(20))
print(auto1.obtener_posicion())
print(auto1.mover(30))