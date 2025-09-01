import pytest
import random
from pytest_mock import mocker

from src.tools.rng import GeneradorAleatorio, GeneradorDeterminista

# Tests generador aleatorio usado en juego real

def test_generar_num_azar_con_randint(mocker):
    mock_randint = mocker.patch('src.tools.rng.random.randint')
    rng = GeneradorAleatorio()
    num = rng.generar(min_num=1, max_num=6)
    mock_randint.assert_called_once_with(1,6)


# Tests generador determinista usado en tests

def test_generar_num_determinista():
    rng = GeneradorDeterminista(num_fijo=1)
    num = rng.generar(min_num=1, max_num=6)
    assert num == rng.num_fijo

def test_generador_determinista_independiente():
    rng1 = GeneradorDeterminista(num_fijo=1)
    rng2 = GeneradorDeterminista(num_fijo=2)

    assert rng1.generar(1,6) == 1
    assert rng2.generar(1,6) == 2
