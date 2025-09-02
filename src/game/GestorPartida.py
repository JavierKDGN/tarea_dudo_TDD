from src.game.Dado import Dado

class GestorPartida:

    def __init__(self, jugadores: list):
        self.jugadores = jugadores
        self.jugador_actual = None

    def get_jugador_actual(self):
        return self.jugador_actual

    def determinar_turno_inicial(self):
        jugadores_dados_map = dict.fromkeys(self.jugadores, 0)
        max_valor = -1
        while len(jugadores_dados_map) > 1:

            for jugador in jugadores_dados_map.keys():
                dado = Dado()
                jugadores_dados_map[jugador] = dado.getValue()

            jugadores_dados_map = dict(sorted(jugadores_dados_map.items(),key=lambda x:x[1], reverse=True))
            max_valor = next(iter(jugadores_dados_map.values()))

            perdedores = []
            for k, v in jugadores_dados_map.items():
                # Eliminamos los perdedores
                if v < max_valor:
                    perdedores.append(k)

            for p in perdedores:
                jugadores_dados_map.pop(p)

        self.jugador_actual = list(jugadores_dados_map)[0]












