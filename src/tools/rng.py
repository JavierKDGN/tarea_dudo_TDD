import random

class GeneradorAleatorio:

    def generar(self, min_num:int, max_num:int):
        return random.randint(min_num, max_num)

class GeneradorDeterminista:
    numero = 1

    def generar(self, min_num:int, max_num:int):
        return self.numero


