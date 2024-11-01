import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_05 import tributa

def test_tributa():
    assert tributa(-1, 1) == "Ha ocurrido un error."
    assert tributa(18, 345) == "No tributa."
    assert tributa(18, 3647) == "Tributa"

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (-1, 1, "Ha ocurrido un error."),
        (18, 345, "No tributa."),
        (18, 2369, "Tributa")
    ]
)

def test_tributa_params(input_x, input_y, expected):
    assert tributa(input_x, input_y) == expected