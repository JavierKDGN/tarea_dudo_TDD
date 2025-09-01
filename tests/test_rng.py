import pytest
from src.tools.rng import GeneradorAleatorio, GeneradorDeterminista

def test_generar_num_azar():
    rng = GeneradorAleatorio()
    num = rng.generar(min_num=1, max_num=6)
    assert num in range(1,7)

def test_generar_num_determinista():
    rng = GeneradorDeterminista(num_fijo=1)
    num = rng.generar(min_num=1, max_num=6)
    assert num == rng.num_fijo

def test_generador_determinista_independiente():
    rng1 = GeneradorDeterminista(num_fijo=1)
    rng2 = GeneradorDeterminista(num_fijo=2)

    assert rng1.generar(1,6) == 1
    assert rng2.generar(1,6) == 2
