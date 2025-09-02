import pytest
from pytest_mock import mocker

from src.game.GestorPartida import GestorPartida

def test_crear_gestor_con_jugadores(mock_jugadores_factory):
    gestor = GestorPartida(mock_jugadores_factory(2))

    assert [p.nombre for p in gestor.jugadores] == ["Jugador1", "Jugador2"]

def test_determinar_turno_inicial(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 1
    # Parcheamos randint para que saque esos valores
    # Side effect causa que se retorne en ese orden
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,1])
    gestor = GestorPartida(mock_jugadores_factory(3))

    # Haremos que Jugador2 empiece
    gestor.determinar_turno_inicial()
    assert gestor.get_jugador_actual().nombre == "Jugador2"

def test_determinar_turno_inicial_empate(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 6
    # Desempate, Jugador2 y Jugador3 volveran a tirar dados (4, 2)
    # Gana Jugador2

    # Parcheamos randint para que saque esos valores
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,6,4,2])

    gestor = GestorPartida(mock_jugadores_factory(3))

    # Deberia haber empate entre jugador2 y jugador3, se vuelve a lanzar el dado entre esos 2
    gestor.determinar_turno_inicial()
    assert gestor.get_jugador_actual().nombre == "Jugador2"

def test_siguiente_turno_2_jugadores(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(2)
    gestor = GestorPartida(jugadores)
    gestor.jugador_actual = gestor.jugadores[0]

    assert gestor.get_jugador_actual() == jugadores[0]

    gestor.avanzar_turno()

    assert gestor.get_jugador_actual() == jugadores[1]
