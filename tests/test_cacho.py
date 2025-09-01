from src.game.Cacho import Cacho

def test_initial_content():
	cacho = Cacho()
	
	assert len(cacho.getDados()) == 5

def test_shake():
	cacho = Cacho()
	
	dados1 = cacho.getDados()
	
	cacho.shake()
	
	dados2 = cacho.getDados()
	
	assert len(dados1) == len(dados2)
	
	# Cannot test if shake was "successful" because it is absolutely possible
	# that both lists have the same values after a shake