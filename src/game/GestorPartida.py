import random

from src.game.ArbitroRonda import ArbitroRonda
from src.game.Jugador import Jugador
from src.game.ValidadorApuesta import Apuesta, ValidadorApuesta


class GestorPartida:

    def __init__(self, jugadores: list):
        self.__jugadores = jugadores
        self.__indice_jugador_actual = 0
        self.__jugador_actual = jugadores[0]
        self.__partida_terminada = False
        self.__apuesta_actual = None
        self.__dados_iniciales = len(jugadores) * 5 # 5 dados de partida cada uno

    def getJugadores(self) -> list[Jugador]:
        return self.__jugadores

    def getJugadorActual(self) -> Jugador:
        return self.__jugadores[self.__indice_jugador_actual]

    def setJugadorActual(self, jugador):
        self.__indice_jugador_actual = self.__jugadores.index(jugador)
        self.__jugador_actual = self.__jugadores[self.__indice_jugador_actual]

    def getApuestaActual(self) -> Apuesta:
        return self.__apuesta_actual

    def setApuestaActual(self, apuesta: Apuesta):
        self.__apuesta_actual = apuesta

    def getPartidaTerminada(self):
        return self.__partida_terminada

    def getJugadorAnterior(self):
        jugador_anterior = self.__jugadores[(self.__indice_jugador_actual - 1) % len(self.__jugadores)]
        return jugador_anterior

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
        if len(self.__jugador_actual.getCacho().getDados()) == 1:
            if ValidadorApuesta.is_correct_special(self.__apuesta_actual, nueva_apuesta):
                self.__apuesta_actual = nueva_apuesta
                self.avanzar_turno()
            else:
                pass
        else:
            if ValidadorApuesta.is_correct(self.__apuesta_actual, nueva_apuesta):
                self.__apuesta_actual = nueva_apuesta
                self.avanzar_turno()
            else:
                pass

    def _iniciar_siguiente_ronda(self):
        # Resetea el estado
        self.setApuestaActual(None)
        # Establece el turno en el jugador de ronda anterior

    def _calcular_total_dados(self):
        total = 0
        for jugador in self.__jugadores:
            total += len(jugador.getCacho().getDados())
        return total

    def _es_valido_calzar(self):
        jugador_con_un_dado = self.getJugadorActual().getCantidadDados() == 1
        mitad_de_dados_en_juego = self._calcular_total_dados() <= self.__dados_iniciales // 2
        return jugador_con_un_dado or mitad_de_dados_en_juego

    def _resolver_ronda_con_ganador_de_dado(self, jugador_ganador):
        jugador_ganador.get_cacho().addDado()

    def dudar(self):
        jugador_apostador = self.getJugadorAnterior()
        jugador_que_duda = self.getJugadorActual()
        apuesta_en_juego = self.getApuestaActual()
        lista_de_jugadores = self.getJugadores()

        (perdedor, resultado) = ArbitroRonda.resolver(
            jugadores=lista_de_jugadores,
            jugador1=jugador_apostador,
            jugador2=jugador_que_duda,
            cantidad_apuesta=apuesta_en_juego.get_amount(),
            pinta=apuesta_en_juego.get_number(),
            accion="dudo"
        )
        #    Reutiliza logica de perdida de un dado y sus consecuencias
        self.resolver_ronda_con_perdedor(perdedor)

        self._iniciar_siguiente_ronda()

    def calzar(self):
        if not self._es_valido_calzar():
            return  # no se hace nada

        # Si es que es valido, recopilar la informacion como en dudar.
        jugador_apostador = self.getJugadorAnterior()
        jugador_que_calza = self.getJugadorActual()
        apuesta_en_juego = self.getApuestaActual()
        lista_de_jugadores = self.getJugadores()

        (jugador_afectado, resultado) = ArbitroRonda.resolver(
            jugadores=lista_de_jugadores,
            jugador1=jugador_apostador,
            jugador2=jugador_que_calza,
            cantidad_apuesta=apuesta_en_juego.get_amount(),
            pinta=apuesta_en_juego.get_number(),
            accion="calzo"
        )


        if resultado == -1:  # El que calzó pierde un dado.
            self.resolver_ronda_con_perdedor(jugador_afectado)
            turno_siguiente_ronda = jugador_afectado
        elif resultado == 1:  # El que calzó gana un dado.
            self._resolver_ronda_con_ganador_de_dado(jugador_afectado)
            turno_siguiente_ronda = jugador_afectado

        self._iniciar_siguiente_ronda()









