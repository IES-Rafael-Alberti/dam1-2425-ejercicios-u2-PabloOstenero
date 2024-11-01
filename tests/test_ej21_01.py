import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_01 import comprueba_mayor

def test_comprueba_mayor():
    assert comprueba_mayor(4) == False
    assert comprueba_mayor(18) == True

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (4, False),
        (23, True),
    ]
)

def test_comprueba_mayor_params(input_x, expected):
    assert comprueba_mayor(input_x) == expected