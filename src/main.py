def test_reroll():
	dado = Dado()
	
	dado.reroll()
	
	assert (dado.value >= 1) and (dado.value <= 6)