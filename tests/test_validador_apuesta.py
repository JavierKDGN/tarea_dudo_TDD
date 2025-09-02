from src.game.ValidadorApuesta import Apuesta
from src.game.ValidadorApuesta import ValidadorApuesta

def test_is_correct():
	validador_apuesta = ValidadorApuesta()
	
	apuestas = [
		(Apuesta(number = 1, amount = 1), False), # Cannot start with 1 (in common rounds)
		(Apuesta(number = 3, amount = 2), True), # Correct, valid start
		(Apuesta(number = 3, amount = 2), False), # Incorrect, same values
		(Apuesta(number = 3, amount = 3), True), # Correct, same number, greater amount
		(Apuesta(number = 2, amount = 4), True), # Correct, smaller number, greater amount
		(Apuesta(number = 4, amount = 2), True), # Correct, greater number, smaller amount
		(Apuesta(number = 5, amount = 3), True), # Correct, can increase both
		(Apuesta(number = 4, amount = 2), False), # Incorrect, both smaller
		(Apuesta(number = 3, amount = 7), True), # Correct, smaller number, greater amount
		(Apuesta(number = 1, amount = 3), False), # Incorrect, moving to 1's but 3 < ((7 // 2) + 1)
		(Apuesta(number = 1, amount = 4), True), # Correct, moving to 1's and 4 >= ((7 // 2) + 1)
		(Apuesta(number = 5, amount = 8), False), # Incorrect, moving from 1's but 8 < ((4 * 2) + 1)
		(Apuesta(number = 5, amount = 9), True) # Correct, moving from 1's and 9 >= ((4 * 2) + 1)
	]
	
	prev = None
	curr = None
		
	for i in range(0, len(apuestas)):
		curr = apuestas[i][0]
		correct = apuestas[i][1]
		
		assert validador_apuesta.is_correct(prev, curr) == correct
		
		if correct:
			prev = curr