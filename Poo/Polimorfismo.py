class Animal():
    def sonido (self):
        pass

class Gato(Animal):
    def sonido(self):
        return 'miau'
class Perro(Animal):
    def sonido(self):
        return 'guau'
def hacer_sonido(animal):
    print(animal.sonido())

gato1 = Gato()
perro1 = Perro()
hacer_sonido(gato1)