import pytest
from pytest_mock import mocker

from src.game.Cacho import Cacho
from src.game.Jugador import Jugador


def test_crear_gestor_con_jugadores():

    mock_jugador1 = mocker.Mock()
    mock_jugador2 = mocker.Mock()

    mock_jugador1.nombre = "Jugador1"
    mock_jugador2.nombre = "Jugador2"

    jugadores = [mock_jugador1, mock_jugador2]
    gestor = GestorPartida(jugadores)

    assert gestor.jugadores = jugadores

