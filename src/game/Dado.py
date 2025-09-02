import random

class Dado:
	def __init__(self):
		self.__name = None
		self.__value = None
		
		self.__MIN_VALUE = 1
		self.__MAX_VALUE = 6
		
		self.__NAMES = {
			1: 'As',
			2: 'Tonto',
			3: 'Tren',
			4: 'Cuadra',
			5: 'Quina',
			6: 'Sexto'
		}
		
		self.roll()
	
	def getName(self):
		return self.__name
	
	def getValue(self):
		return self.__value
	
	def setValue(self, value):
		self.__value = value
		self.__name = self.__NAMES[self.__value]
	
	def roll(self):
		self.setValue(random.randint(self.__MIN_VALUE, self.__MAX_VALUE))