import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_11 import invertir_palabra

def test_invertir_palabra():
    assert invertir_palabra("Hola") == "aloH"
    assert invertir_palabra("Que tal") == "lat euQ"
    assert invertir_palabra("Vox Machina") == "anihcaM xoV"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("Hola", "aloH"),
        ("Que tal", "lat euQ"),
        ("Vox Machina", "anihcaM xoV"),
    ]
)

def test_invertir_palabra_params(input_x, expected):
    assert invertir_palabra(input_x) == expected