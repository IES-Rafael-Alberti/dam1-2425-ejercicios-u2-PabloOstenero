import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_04 import mostrar_cuenta_atras

def test_mostrar_cuenta_atras():
    assert mostrar_cuenta_atras(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"
    assert mostrar_cuenta_atras(5) == "5, 4, 3, 2, 1, 0"
    assert mostrar_cuenta_atras(1) == "1, 0"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (5, "5, 4, 3, 2, 1, 0"),
        (1, "1, 0"),
    ]
)

def test_mostrar_cuenta_atras_params(input_x, expected):
    assert mostrar_cuenta_atras(input_x) == expected