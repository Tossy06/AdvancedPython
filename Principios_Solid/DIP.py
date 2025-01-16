'''
Inverción de dependencias:
1: Los modulos de alto nivel no deben depender de los de alto nivel, si no que los dos deben
depender de las abstracciones
2: Las abstraciones no deben depender de implementaciones especificas
'''

'''
class Diccionario:
    def verificar_palabra(self, palabra):
        #logica para verificar palabras
        pass

class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        #usamos el diccionario para corregir texto
        pass        
'''

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si está en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #usamos el verificadro para corregir texto
        pass

corrector = CorrectorOrtografico(ServicioOnline())