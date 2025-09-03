from pytest_mock import mocker
from src.game.ArbitroRonda import ArbitroRonda

from src.game.Cacho import Cacho
from src.game.Jugador import Jugador
from src.game.Dado import Dado
def make_dado(n):
    d = Dado()
    d.setValue(n)
    return d
def test_dudo_correcto():
    jugador1 = Jugador("Alice",Cacho())
    jugador2 = Jugador("Bob",Cacho())
    jugadores = [jugador1,jugador2,Jugador("Carol",Cacho())]
    cantidad_apuesta,pinta = 5,4

    valores_dados = [
        [2,4,4],
        [1,2,5,5],
        [3,2,6,6]
    ]

    for i in range(3):
        dados = [make_dado(val) for val in valores_dados[i]]
        mocker.patch.object(jugadores[i].cacho,"getDados",return_value=dados)

    assert ArbitroRonda.resolver(jugadores,jugador1,jugador2,cantidad_apuesta,pinta,"dudo") == (jugador1,-1)
def test_dudo_incorrecto():
    jugador1 = Jugador("Alice",Cacho())
    jugador2 = Jugador("Bob",Cacho())
    jugadores = [jugador1,jugador2,Jugador("Carol",Cacho())]
    cantidad_apuesta,pinta = 3,4

    valores_dados = [
        [2,4,4],
        [1,1,5,5],
        [3,2,4,6]
    ]

    for i in range(3):
        dados = [make_dado(val) for val in valores_dados[i]]
        mocker.patch.object(jugadores[i].cacho,"getDados",return_value=dados)

    assert ArbitroRonda.resolver(jugadores,jugador1,jugador2,cantidad_apuesta,pinta,"dudo") == (jugador2,-1)
def test_calzo_correcto():
    jugador1 = Jugador("Alice",Cacho())
    jugador2 = Jugador("Bob",Cacho())
    jugadores = [jugador1,jugador2,Jugador("Carol",Cacho())]
    cantidad_apuesta,pinta = 5,3

    valores_dados = [
        [2,3,3],
        [1,1,5,5],
        [3,2,4,6]
    ]

    for i in range(3):
        dados = [make_dado(val) for val in valores_dados[i]]
        mocker.patch.object(jugadores[i].cacho,"getDados",return_value=dados)

    assert ArbitroRonda.resolver(jugadores,jugador1,jugador2,cantidad_apuesta,pinta,"calzo") == (jugador2,1)
def test_calzo_incorrecto():
    jugador1 = Jugador("Alice",Cacho())
    jugador2 = Jugador("Bob",Cacho())
    jugadores = [jugador1,jugador2,Jugador("Carol",Cacho())]
    cantidad_apuesta,pinta = 1,3

    valores_dados = [
        [2,3,3],
        [1,1,5,5],
        [3,2,4,6]
    ]

    for i in range(3):
        dados = [make_dado(val) for val in valores_dados[i]]
        mocker.patch.object(jugadores[i].cacho,"getDados",return_value=dados)

    assert ArbitroRonda.resolver(jugadores,jugador1,jugador2,cantidad_apuesta,pinta,"calzo") == (jugador2,-1)