'''
Sustitución de liscope: Si la clase b, es una subclase de la clase a
la clase a, deberia poder utilizarse en todo los lugares donde b pueda utilizarse
'''
'''
class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return 'No puedo volar'
    

def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))
'''

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando'
    
class AveNoVoladora(Ave):
    pass