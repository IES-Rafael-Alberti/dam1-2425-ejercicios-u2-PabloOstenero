import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_10 import primo_o_no_primo

def test_primo_o_no_primo():
    assert primo_o_no_primo(10) == True
    assert primo_o_no_primo(5) == False
    assert primo_o_no_primo(1) == True

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (10, True),
        (5, False),
        (1, True),
    ]
)

def test_primo_o_no_primo_params(input_x, expected):
    assert primo_o_no_primo(input_x) == expected