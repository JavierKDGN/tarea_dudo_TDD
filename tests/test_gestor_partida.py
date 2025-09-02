import pytest
import pytest_mock
from pytest_mock import mocker

from src.game.Cacho import Cacho
from src.game.Jugador import Jugador
from src.game.GestorPartida import GestorPartida

@pytest.fixture
def mock_2_jugadores(mocker):
    mock_jugador1 = mocker.Mock(nombre = "Jugador1")
    mock_jugador2 = mocker.Mock(nombre = "Jugador2")

    jugadores = [mock_jugador1, mock_jugador2]
    return jugadores


def test_crear_gestor_con_jugadores(mock_2_jugadores):
    gestor = GestorPartida(mock_2_jugadores)

    assert [p.nombre for p in gestor.jugadores] == ["Jugador1", "Jugador2"]

def test_tirar_dado_inicial_cada_jugador(mocker):

    mock_cacho_jugador = mocker.Mock()
    mock_cacho_jugador.getDados.return_value = [None] * 5

    jugador = Jugador(nombre="test", cacho = mock_cacho_jugador)
    dado = jugador.tirar_dado_inicial()

    assert dado == 5
