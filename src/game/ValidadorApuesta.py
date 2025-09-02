class Apuesta:
	def __init__(self, number, amount):
		self.__number = number
		self.__amount = amount
	
	def get_number(self):
		return self.__number
	
	def get_amount(self):
		return self.__amount

class ValidadorApuesta:
	@staticmethod
	def is_correct(prev, curr):
		if prev == None:
			if curr.get_number() == 1:
				return False
			
			return True
		
		# Moving to 1's
		if (prev.get_number() != 1) and (curr.get_number() == 1):
			if curr.get_amount() < ((prev.get_amount() // 2) + 1):
				return False
			
			return True
		
		# Moving from 1's
		if (prev.get_number() == 1) and (curr.get_number() != 1):
			if curr.get_amount() < ((prev.get_amount() * 2) + 1):
				return False
			
			return True
		
		if (prev.get_number() >= curr.get_number()) and (prev.get_amount() >= curr.get_amount()):
			return False
		
		return True