from src.game.Dado import Dado

class Cacho:
	__dados = []
	
	def __init__(self):
		for i in range(0, 5):
			self.__dados.append(Dado())
	
	def getDados(self):
		return self.__dados