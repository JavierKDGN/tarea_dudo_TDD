import pytest
from src.tools.rng import GeneradorAleatorio

def test_generar_num_azar():
    rng = GeneradorAleatorio()
    num = rng.generar(min_num=1, max_num=6)
    assert num in range(1,7)