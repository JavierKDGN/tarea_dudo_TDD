import random

class GeneradorAleatorio:

    def generar(self, min_num:int, max_num:int):
        return random.randint(min_num, max_num)

class GeneradorDeterminista:
    numero = 1

    def __init__(self, num_fijo: int):
        self.num_fijo = num_fijo

    def generar(self, min_num:int, max_num:int):
        return self.num_fijo


