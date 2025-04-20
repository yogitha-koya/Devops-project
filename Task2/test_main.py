import pytest
from main import calculate_average

def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
    assert round(calculate_average([1.5, 2.5, 3.0]), 2) == 2.33


