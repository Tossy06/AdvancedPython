class Personaje():
    def __init__(self, nick, vida):
        self.nick = nick
        self.vida = vida
    def recibir_daño(self, daño_recibido):
        if daño_recibido > 0:
            self.vida -= daño_recibido
            if self.vida <= 0:
                self.vida = 0
                print(f'{self.nick} ha recibido daño y ha muerto')
            else:
                print(f'{self.nick}, ha recibido {daño_recibido} de daño. Vida restante {self.vida}')
class Player(Personaje):
    def __init__(self, nick, vida, daño_a_enemigo):
        super().__init__(nick, vida)
        self.daño_a_enemigo = daño_a_enemigo
    def hacer_daño(self, enemigo):
        if isinstance(enemigo, Personaje):
            print(f'{self.nick} ataco a {enemigo.nick} causando {self.daño_a_enemigo} de daño')
            enemigo.recibir_daño(self.daño_a_enemigo)

class Enemigo(Personaje):
    def __init__(self, nick, vida, daño_a_jugador):
        super().__init__(nick, vida)
        self.daño_a_jugador = daño_a_jugador
    def hacer_daño(self, jugador):
        if isinstance(jugador, Personaje):
            print(f'{self.nick} ataco a {jugador.nick} causando {self.daño_a_jugador} de daño')
            jugador.recibir_daño(self.daño_a_jugador)

player1 = Player('Tossy', 100, 50)
enemy= Enemigo('Destrozador', 200, 75)
player1.hacer_daño(enemy)
enemy.hacer_daño(player1)


    
        

    


        