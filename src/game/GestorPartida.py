from src.game.Dado import Dado

class GestorPartida:

    def __init__(self, jugadores: list):
        self.jugadores = jugadores
        self.jugador_actual = None

    def get_jugador_actual(self):
        return self.jugador_actual

    def determinar_turno_inicial(self):
        max_valor = 0
        for jugador in self.jugadores:
            # Cada jugador tira un dado, este no forma parte del cacho ya que es solo para determinar el turno
            dado = Dado()
            if dado.getValue() > max_valor:
                self.jugador_actual = jugador
                max_valor = dado.getValue()



