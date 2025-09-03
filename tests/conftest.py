import pytest

@pytest.fixture
def mock_jugadores_factory(mocker):
    '''
    Al hacer tests me di cuenta que se repetia el mock de jugadores
    y a veces necesitaba 2 jugadores o mas, por lo que
    este fixture de pytest resume este proceso y permita ajustar
    la cantidad de jugador en cada llamada
    '''
    def _create(num_jugadores: int, num_dados_por_jugador: int = 5):
        jugadores = []
        for i in range(num_jugadores):
            jugador = mocker.Mock()
            jugador.nombre = f"Jugador{i+1}"
            jugador.cacho = mocker.Mock()
            jugador.cacho.getDados.return_value = [None] * num_dados_por_jugador
            jugador.cacho.removeDado.return_value = None
            jugador.get_cantidad_dados.return_value = num_dados_por_jugador

            jugadores.append(jugador)
        return jugadores
    return _create