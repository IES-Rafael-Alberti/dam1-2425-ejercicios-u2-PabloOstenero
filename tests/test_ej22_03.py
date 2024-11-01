import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_03 import mostrar_impares

def test_mostrar_impares():
    assert mostrar_impares(10) == "1, 3, 5, 7, 9"
    assert mostrar_impares(5) == "1, 3, 5"
    assert mostrar_impares(1) == "1"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (10, "1, 3, 5, 7, 9"),
        (5, "1, 3, 5"),
        (1, "1"),
    ]
)

def test_mostrar_impares_params(input_x, expected):
    assert mostrar_impares(input_x) == expected