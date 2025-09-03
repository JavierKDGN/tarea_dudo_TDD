import random

from src.game.Jugador import Jugador


class GestorPartida:

    def __init__(self, jugadores: list):
        self.__jugadores = jugadores
        self.__jugador_actual = None

    def get_jugadores(self) -> list[Jugador]:
        return self.__jugadores

    def get_jugador_actual(self) -> Jugador:
        return self.__jugador_actual

    def set_jugador_actual(self, jugador):
        self.__jugador_actual = jugador

    def determinar_turno_inicial(self):
        jugadores_dados_map = dict.fromkeys(self.__jugadores, 0)
        max_valor = -1
        while len(jugadores_dados_map) > 1:

            for jugador in jugadores_dados_map.keys():
                dado = random.randint(1,6)
                jugadores_dados_map[jugador] = dado

            jugadores_dados_map = dict(sorted(jugadores_dados_map.items(),key=lambda x:x[1], reverse=True))
            max_valor = next(iter(jugadores_dados_map.values()))

            perdedores = []
            for k, v in jugadores_dados_map.items():
                # Eliminamos los perdedores
                if v < max_valor:
                    perdedores.append(k)

            for p in perdedores:
                jugadores_dados_map.pop(p)

        self.__jugador_actual = list(jugadores_dados_map)[0]

    def avanzar_turno(self):
        idx = self.__jugadores.index(self.__jugador_actual)
        self.__jugador_actual = self.__jugadores[(idx + 1) % len(self.__jugadores)]

    def perdida_de_dado(self, jugador_perdedor: Jugador):
        jugador_perdedor.get_cacho().removeDado()
        if len(jugador_perdedor.get_cacho().getDados()) == 0:
            self.__jugadores.remove(jugador_perdedor)











