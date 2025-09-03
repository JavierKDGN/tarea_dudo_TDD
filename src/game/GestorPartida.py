import random

from src.game.Jugador import Jugador
from src.game.ValidadorApuesta import Apuesta, ValidadorApuesta


class GestorPartida:

    def __init__(self, jugadores: list):
        self.__jugadores = jugadores
        self.__jugador_actual = None
        self.__indice_jugador_actual = 0
        self.__partida_terminada = False
        self.__apuesta_actual = None

    def getJugadores(self) -> list[Jugador]:
        return self.__jugadores

    def getJugadorActual(self) -> Jugador:
        return self.__jugadores[self.__indice_jugador_actual]

    def setJugadorActual(self, jugador):
        self.__indice_jugador_actual = self.__jugadores.index(jugador)

    def getApuestaActual(self) -> Apuesta:
        return self.__apuesta_actual

    def setApuestaActual(self, apuesta: Apuesta):
        self.__apuesta_actual = apuesta

    def getPartidaTerminada(self):
        return self.__partida_terminada

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
        self.__indice_jugador_actual = self.__jugadores.index(self.__jugador_actual)

    def avanzar_turno(self):
        self.__indice_jugador_actual += 1
        self.__jugador_actual = self.__jugadores[(self.__indice_jugador_actual) % len(self.__jugadores)]

    def _quitar_dado_a_jugador(self, jugador: Jugador):
        jugador.getCacho().removeDado()

    def _verificar_eliminacion_jugador(self, jugador: Jugador):
        if len(jugador.getCacho().getDados()) == 0:
            idx = self.__jugadores.index(jugador)
            self.__jugadores.pop(idx)
            if idx <= self.__indice_jugador_actual:
                self.__indice_jugador_actual -= 1

    def _verificar_condicion_victoria(self):
        if len(self.__jugadores) == 1:
            self.__jugador_actual = self.__jugadores.pop()
            self.__partida_terminada = True

    def resolver_ronda_con_perdedor(self, jugador_perdedor: Jugador):
        self._quitar_dado_a_jugador(jugador_perdedor)
        self._verificar_eliminacion_jugador(jugador_perdedor)
        self._verificar_condicion_victoria()

    def recibir_apuesta(self, nueva_apuesta: Apuesta):
        if ValidadorApuesta.is_correct(self.__apuesta_actual, nueva_apuesta):
            self.__apuesta_actual = nueva_apuesta
            self.avanzar_turno()
        else:
            pass


    def perdida_de_dado(self, jugador_perdedor: Jugador):
        jugador_perdedor.getCacho().removeDado()
        if len(jugador_perdedor.getCacho().getDados()) == 0:
            self.__jugadores.remove(jugador_perdedor)
            if len(self.__jugadores) == 1:
                self.__jugador_actual = self.__jugadores[0]
                self.__partida_terminada = True











