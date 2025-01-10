class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    

david = Persona('David', 18)

nombre = david.nombre
print(nombre)

david.nombre = 'Pepe'

nombre = david.nombre
print(nombre)

