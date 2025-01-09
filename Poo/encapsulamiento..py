'''
class mi_encap:
    def __init__(self):
        self.__atributo_privado = 'valor'

objeto = mi_encap()
print(objeto.__atributo_privado)
'''
#Getter y Setter
class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

david = Persona('David', 18)
nombre = david.get_nombre()
print(nombre)
