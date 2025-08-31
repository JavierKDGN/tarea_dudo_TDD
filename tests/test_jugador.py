import pytest

def test_jugador_inicia_con_5_dados():
    jugador = Jugador()
    assert jugador.get_cantidad_dados() == 5