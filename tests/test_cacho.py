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

def test_insert():
	cacho = Cacho()
	
	len1 = len(cacho.getDados())
	cacho.insertDado()
	len2 = len(cacho.getDados())
	
	assert len2 == len1 + 1

def test_remove():
	cacho = Cacho()
	
	len1 = len(cacho.getDados())
	cacho.removeDado()
	len2 = len(cacho.getDados())
	
	assert len2 == len1 - 1

def test_dados_distintos_cachos_independientes():
	# Bug: Distintas instancias de Cachos comparten la misma lista de dados
	# Solucion: Mover lista de dados al constructor en vez de ser atributo de clase
	
	cacho1 = Cacho()
	
	assert len(cacho1.getDados()) == 5
	
	cacho2 = Cacho()
	cacho2.removeDado()
	
	assert len(cacho1.getDados()) == 5