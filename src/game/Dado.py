import random

class Dado:
	value = None
	
	__MIN_VALUE = 1
	__MAX_VALUE = 6
	
	def __init__(self):
		self.value = random.randint(self.__MIN_VALUE, self.__MAX_VALUE)
	
	def reroll(self):
		self.value = random.randint(self.__MIN_VALUE, self.__MAX_VALUE)