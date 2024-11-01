import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_17 import suma_digitos

def test_suma_digitos():
    assert suma_digitos(-1) == "El número tenía que ser positivo."
    assert suma_digitos(5) == "La suma de los dígitos es 5"
    assert suma_digitos(23) == "La suma de los dígitos es 5"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (-1, "El número tenía que ser positivo."),
        (5, "La suma de los dígitos es 5"),
        (23, "La suma de los dígitos es 5"),
    ]
)

def test_suma_digitos_params(input_x, expected):
    assert suma_digitos(input_x) == expected