from src.game.Cacho import Cacho

def test_initial_content():
	cacho = Cacho()
	
	assert len(cacho.getDados()) == 5