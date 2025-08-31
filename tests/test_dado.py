from src.game.Dado import Dado

def test_value():
	dado = Dado()
	
	assert (dado.value >= 1) and (dado.value <= 6)