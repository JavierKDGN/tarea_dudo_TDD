import pytest
from src.game.Jugador import Jugador

def test_jugador_inicia_con_5_dados(mocker):
    # Creamos un Mock del cacho del jugador
    mock_cacho_jugador = mocker.Mock()
    # El Cacho inicia con 5 dados al empezar la partida
    mock_cacho_jugador.getDados.return_value = [None] * 5

    jugador = Jugador(nombre="test", cacho = mock_cacho_jugador)
    assert jugador.getCantidadDados() == 5