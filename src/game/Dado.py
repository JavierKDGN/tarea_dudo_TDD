import random

class Dado:
	__name = None
	__value = None
	
	__MIN_VALUE = 1
	__MAX_VALUE = 6
	
	__NAMES = {
		1: 'As',
		2: 'Tonto',
		3: 'Tren',
		4: 'Cuadra',
		5: 'Quina',
		6: 'Sexto'
	}
	
	def __init__(self):
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