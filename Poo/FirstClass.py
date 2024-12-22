'''
class Celular():
    ram = 15
    pantalla ='oled'
    alamacenamiento = 255
    camaras = 'Tres camaras, dos de 24 mega pixeles y una de 100 mega pixeles'
    marca = 'Xiaomi'
    modelo = '100'

Celular1 = Celular()
print(Celular1.camaras)
'''

class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def encender (self):
        print(f'El auto de la marca {self.marca}, esta encendido')
    def apagar (self):
        print(f'El auto de la marca {self.marca}, esta apagado')

auoto1 = Auto('mclaren', 'zenna', 400.000)
auoto2 = Auto('koenihsegg', 'gemera', 700.000)
'''
print(auoto1.marca)
print(auoto2.marca)
'''
auoto1.encender()
auoto2.apagar()