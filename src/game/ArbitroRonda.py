from src.game.Jugador import Jugador
from src.game.Cacho import Cacho
from src.game.ContadorPintas import ContadorPintas
class ArbitroRonda:
    @staticmethod
    def resolver(jugadores, jugador1,jugador2,cantidad_apuesta,pinta,accion):
        """Resuelve el resultado de una ronda de dudo o calzo.

                Args:
                    jugadores (list[Jugador]): Lista de todos los jugadores en la ronda.
                    jugador1 (Jugador): El jugador que hizo la apuesta.
                    jugador2 (Jugador): El jugador que responde (dudo o calzo).
                    cantidad_apuesta (int): La cantidad de dados apostada.
                    pinta (int): El valor de dado (1–6) que se apuesta.
                    accion (str): La acción realizada, "dudo" o "calzo".

                Returns:
                    tuple: (jugador, resultado), donde:
                        - jugador (Jugador): El jugador que pierde o gana.
                        - resultado (int): -1 si pierde, 1 si gana.
                          En caso de acción inválida, retorna -1.
                """
        dados = [dado for j in jugadores for dado in j.cacho.getDados()]

        cantidad_pinta = ContadorPintas.contar(dados,pinta)
        if accion == "dudo":
            if cantidad_pinta < cantidad_apuesta:
                return jugador1,-1
            else:
                return jugador2,-1
        elif accion == "calzo":
            if cantidad_pinta == cantidad_apuesta:
                return jugador2,1
            else:
                return jugador2,-1
        else:
            raise ValueError(f"Acción inválida: {accion}")
