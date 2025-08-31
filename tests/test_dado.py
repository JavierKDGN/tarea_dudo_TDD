from src.game.Dado import Dado

def test_value():
	dado = Dado()
	
	assert (dado.value >= 1) and (dado.value <= 6)

def test_reroll():
	dado = Dado()
	
	dado.reroll()
	
	assert (dado.value >= 1) and (dado.value <= 6)