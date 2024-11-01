import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_25 import palabra_mas_larga

def test_palabra_mas_larga():
    assert palabra_mas_larga("Hola buenas") == "La palabra más larga de la frase Hola buenas es buenas"
    assert palabra_mas_larga("Como esta hoy Paco") == "La palabra más larga de la frase Como esta hoy Paco es Como"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("Hola buenas", "La palabra más larga de la frase Hola buenas es buenas"),
        ("Como esta hoy Paco", "La palabra más larga de la frase Como esta hoy Paco es Como"),
    ]
)

def test_palabra_mas_larga_params(input_x, expected):
    assert palabra_mas_larga(input_x) == expected