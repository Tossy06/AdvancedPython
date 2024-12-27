class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentrase(self):
        print(f'Hola mi nombre es: {self.nombre} y mi edad es {self.edad}')

class Estudiante (Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def imprimir_grado(self):
        print(f'Hola soy un estudiante y mi grado es: {self.grado}')

estudiante1 = Estudiante('David', '16', '11')
estudiante1.presentrase()
estudiante1.imprimir_grado()