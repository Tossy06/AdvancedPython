class Personaje:
    def __init__(self, rol, nombre, vida):
        self.rol = rol
        self.nombre = nombre
        self.vida = vida

class Player(Personaje):
    def __init__(self, rol, nombre, vida, daño_a_enemigo, escudo):
        super().__init__(rol,nombre,vida)
        self.daño_a_enemigo = daño_a_enemigo
        self.escudo = escudo
        
class Skills:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad (self):
        print(f'Mi habilidad es: {self.habilidad}')

class Enemigo_con_habilidad (Personaje, Skills):
    def __init__(self, rol, nombre, vida, habilidad, ataque_a_jugador):
        Personaje.__init__(self, rol, nombre, vida)
        Skills.__init__(self, habilidad)
        self.ataque_a_jugador = ataque_a_jugador
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'

        
enemigo1 = Enemigo_con_habilidad('enemigo', 'cataclismo', 100, 'destrucción total', '150')
enemigo1.presentarse()