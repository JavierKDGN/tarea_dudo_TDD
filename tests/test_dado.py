from src.game.Dado import Dado

def test_value():
	dado = Dado()
	
	assert (dado.getValue() >= 1) and (dado.getValue() <= 6)
	
	for i in range(1, 7):
		dado.setValue(i)
		
		assert (dado.getValue() == i)

def test_roll():
	dado = Dado()
	
	dado.roll()
	
	assert (dado.getValue() >= 1) and (dado.getValue() <= 6)

def test_name():
	value_to_name = {
		1: 'As',
		2: 'Tonto',
		3: 'Tren',
		4: 'Cuadra',
		5: 'Quina',
		6: 'Sexto'
	}
	
	for value in value_to_name:
		dado = Dado()
		dado.setValue(value)
		
		assert (dado.getName() == value_to_name[value])