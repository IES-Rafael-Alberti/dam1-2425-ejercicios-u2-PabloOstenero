import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.depuracion.ej24_01 import burbuja

def test_burbuja():
    assert burbuja(['23', '10', '43', '34']) == "10 23 34 43"
    assert burbuja(['23' 'a' '15']) == "La cadena está mal creada."

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (['23', '10', '43', '34'], "10 23 34 43"),
        (['23' 'a' '15'], "La cadena está mal creada.")
    ]
)

def test_burbuja_params(input_x, expected):
    assert burbuja(input_x) == expected