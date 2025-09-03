import pytest
from pytest_mock import mocker

from src.game.GestorPartida import GestorPartida
from src.game.ValidadorApuesta import ValidadorApuesta, Apuesta


def test_crear_gestor_con_jugadores(mock_jugadores_factory):
    gestor = GestorPartida(mock_jugadores_factory(2))

    assert [p.getNombre() for p in gestor.getJugadores()] == ["Jugador1", "Jugador2"]

def test_determinar_turno_inicial(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 1
    # Parcheamos randint para que saque esos valores
    # Side effect causa que se retorne en ese orden
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,1])
    gestor = GestorPartida(mock_jugadores_factory(3))

    # Haremos que Jugador2 empiece
    gestor.determinar_turno_inicial()
    assert gestor.getJugadorActual().getNombre() == "Jugador2"

def test_determinar_turno_inicial_empate(mock_jugadores_factory, mocker):
    # 3 jugadores, sus dados seran 1, 6, 6
    # Desempate, Jugador2 y Jugador3 volveran a tirar dados (4, 2)
    # Gana Jugador2

    # Parcheamos randint para que saque esos valores
    mocker.patch('src.game.GestorPartida.random.randint', side_effect=[1,6,6,4,2])

    gestor = GestorPartida(mock_jugadores_factory(3))

    # Deberia haber empate entre jugador2 y jugador3, se vuelve a lanzar el dado entre esos 2
    gestor.determinar_turno_inicial()
    assert gestor.getJugadorActual().getNombre() == "Jugador2"

def test_siguiente_turno_2_jugadores(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(2)
    gestor = GestorPartida(jugadores)
    gestor.setJugadorActual(gestor.getJugadores()[0])

    assert gestor.getJugadorActual() == jugadores[0]

    gestor.avanzar_turno()

    assert gestor.getJugadorActual() == jugadores[1]

def test_gestor_llama_a_removeDado_del_perdedor(mock_jugadores_factory, mocker):
    # Mock 1 jugador
    jugadores = mock_jugadores_factory(1)
    jugador_perdedor = jugadores[0]

    gestor = GestorPartida(jugadores)
    mock_cacho = jugador_perdedor.getCacho()

    gestor.resolver_ronda_con_perdedor(jugador_perdedor)

    mock_cacho.removeDado.assert_called_once()

def test_jugador_eliminado_cuando_pierde_dados(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(3, 1) # 3 jugadores con 1 dado
    jugador_perdedor = jugadores[0]
    gestor = GestorPartida(jugadores)

    gestor.resolver_ronda_con_perdedor(jugador_perdedor)

    assert jugador_perdedor not in gestor.getJugadores()
    assert len(gestor.getJugadores()) == 2

def test_turnos_mantenidos_tras_eliminacion(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(3,1) # 3 jugadores, 1 dado cada uno
    jugador_perdedor = jugadores[1]
    jugador_perdedor_nombre = jugador_perdedor.getNombre()

    gestor = GestorPartida(jugadores)
    gestor.setJugadorActual(jugador_perdedor)
    gestor.resolver_ronda_con_perdedor(jugador_perdedor)

    assert gestor.getJugadorActual().getNombre() != jugador_perdedor_nombre


def test_partida_termina_cuando_solo_queda_uno(mock_jugadores_factory):
    jugadores = mock_jugadores_factory(2, 1) # 2 jugadores, 1 dado
    jugador_perdedor = jugadores[0]
    gestor = GestorPartida(jugadores)
    gestor.resolver_ronda_con_perdedor(jugador_perdedor)

    assert gestor.getPartidaTerminada() == True

def test_gestor_acepta_apuesta_valida_ronda_normal(mock_jugadores_factory, mocker):
    jugadores = mock_jugadores_factory(2, 2) #2 j, 2 d
    mocker.patch('src.game.GestorPartida.ValidadorApuesta.is_correct', return_value=True)
    nueva_apuesta = mocker.Mock()

    gestor = GestorPartida(jugadores)
    jugador_inicial = gestor.getJugadorActual()
    gestor.recibir_apuesta(nueva_apuesta)
    jugador_final = gestor.getJugadorActual()

    assert gestor.getApuestaActual() == nueva_apuesta
    assert jugador_inicial != jugador_final

def test_gestor_rechaza_apuesta_invalida_ronda_normal(mock_jugadores_factory, mocker):
    jugadores = mock_jugadores_factory(2, 2)
    mocker.patch('src.game.GestorPartida.ValidadorApuesta.is_correct', return_value=False)
    vieja_apuesta = mocker.Mock()
    nueva_apuesta = mocker.Mock()

    gestor = GestorPartida(jugadores)
    gestor.setApuestaActual(vieja_apuesta)
    jugador_inicial = gestor.getJugadorActual()

    gestor.recibir_apuesta(nueva_apuesta)

    jugador_final = gestor.getJugadorActual()

    assert gestor.getApuestaActual() == vieja_apuesta
    assert jugador_inicial == jugador_final








