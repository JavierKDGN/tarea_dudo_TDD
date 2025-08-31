from src.game.Dado import Dado

def test_value():
	dado = Dado()
	
	assert (dado.getValue() >= 1) and (dado.getValue() <= 6)
	
	for i in range(1, 7):
		dado.setValue(i)
		
		assert (dado.getValue() == i)

def test_reroll():
	dado = Dado()
	
	dado.reroll()
	
	assert (dado.getValue() >= 1) and (dado.getValue() <= 6)