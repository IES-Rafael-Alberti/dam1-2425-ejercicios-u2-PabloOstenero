import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_12 import numero_letra_en_frase

def test_numero_letra_en_frase():
    assert numero_letra_en_frase("Hola", "a") == "La letra a está 1 vez en la frase Hola"
    assert numero_letra_en_frase("Pedro va al parque", "e") == "La letra e está 2 veces en la frase Pedro va al parque"
    assert numero_letra_en_frase("Vox Machina", "s") == "La letra s está 0 veces en la frase Vox Machina"

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        ("Hola", "a", "La letra a está 1 vez en la frase Hola"),
        ("Pedro va al parque", "e", "La letra e está 2 veces en la frase Pedro va al parque"),
        ("Vox Machina", "s", "La letra s está 0 veces en la frase Vox Machina")
    ]
)

def test_numero_letra_en_frase_params(input_x, input_y, expected):
    assert numero_letra_en_frase(input_x, input_y) == expected