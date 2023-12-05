from .lab5 import division
import pytest


def test_standard_dividing():
    assert division(2, 2) == 1


def test_dividing_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)
