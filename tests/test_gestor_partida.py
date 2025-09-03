import pytest
from pytest_mock import mocker

from src.game.GestorPartida import GestorPartida

def test_crear_gestor_con_jugadores(mock_jugadores_factory):
    gestor = GestorPartida(mock_jugadores_factory(2))

    assert [p.get_nombre() for p in gestor.get_jugadores()] == ["Jugador1", "Jugador2"]

def test_determinar_turno_inicial(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 1
    # Parcheamos randint para que saque esos valores
    # Side effect causa que se retorne en ese orden
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,1])
    gestor = GestorPartida(mock_jugadores_factory(3))

    # Haremos que Jugador2 empiece
    gestor.determinar_turno_inicial()
    assert gestor.get_jugador_actual().get_nombre()== "Jugador2"

def test_determinar_turno_inicial_empate(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 6
    # Desempate, Jugador2 y Jugador3 volveran a tirar dados (4, 2)
    # Gana Jugador2

    # Parcheamos randint para que saque esos valores
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,6,4,2])

    gestor = GestorPartida(mock_jugadores_factory(3))

    # Deberia haber empate entre jugador2 y jugador3, se vuelve a lanzar el dado entre esos 2
    gestor.determinar_turno_inicial()
    assert gestor.get_jugador_actual().get_nombre() == "Jugador2"

def test_siguiente_turno_2_jugadores(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(2)
    gestor = GestorPartida(jugadores)
    gestor.set_jugador_actual(gestor.get_jugadores()[0])

    assert gestor.get_jugador_actual() == jugadores[0]

    gestor.avanzar_turno()

    assert gestor.get_jugador_actual() == jugadores[1]

def test_gestor_llama_a_removeDado_del_perdedor(mock_jugadores_factory, mocker):
    # Mock 1 jugador
    jugadores = mock_jugadores_factory(1)
    jugador_perdedor = jugadores[0]

    gestor = GestorPartida(jugadores)
    mock_cacho = jugador_perdedor.get_cacho()

    gestor.perdida_de_dado(jugador_perdedor)

    mock_cacho.removeDado.assert_called_once()




