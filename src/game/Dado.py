import random

class Dado:
	__value = None
	
	__MIN_VALUE = 1
	__MAX_VALUE = 6
	
	def __init__(self):
		self.reroll()
	
	def getValue(self):
		return self.__value
	
	def setValue(self, value):
		self.__value = value
	
	def reroll(self):
		self.setValue(random.randint(self.__MIN_VALUE, self.__MAX_VALUE))