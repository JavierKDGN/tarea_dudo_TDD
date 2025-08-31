import random

class Dado:
	__value = None
	
	__MIN_VALUE = 1
	__MAX_VALUE = 6
	
	def __init__(self):
		self.roll()
	
	def getValue(self):
		return self.__value
	
	def setValue(self, value):
		self.__value = value
	
	def roll(self):
		self.setValue(random.randint(self.__MIN_VALUE, self.__MAX_VALUE))