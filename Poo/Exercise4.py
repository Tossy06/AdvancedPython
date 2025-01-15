class Personaje ():
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    
    
    def __repr__(self):
        return f'Personaje ("{self.nombre}", {self.poder})'

    def __add__ (self, fusion):
        nuevo_personaje = round(((self.poder + fusion.poder)/2)**2)
        return Personaje (self.nombre + fusion.nombre, nuevo_personaje)
    
goku = Personaje('Goku', 10000000)
tenshinhan = Personaje('Tenshinhan', 100000)

nuevo_personaje = goku + tenshinhan
print(nuevo_personaje)
        
