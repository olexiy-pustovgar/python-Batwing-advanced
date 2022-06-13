import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(-100, 100) == 0
    assert Calculator.add(210, 33) == 243


def test_subtract():
    assert Calculator.subtract(-10, 13) == -23
    assert Calculator.subtract(-5, -35) == 30
    assert Calculator.subtract(11, 3) == 8


def test_multiply():
    assert Calculator.multiply(11, 11) == 121
    assert Calculator.multiply(-5, 2) == -10
    assert Calculator.multiply(-5, -2) == 10


def test_divide():
    assert Calculator.divide(11, 11) == 1
    assert Calculator.divide(-10, -2) == 5
    assert Calculator.divide(5, -10) == -0.5
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)


