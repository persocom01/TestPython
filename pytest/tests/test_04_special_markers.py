# Demonstrates the xfail and skip markers.
import math
import pytest


@pytest.mark.xfail
def test_x_sqrt(input):
    n = input
    assert math.sqrt(n) == 5


@pytest.mark.xfail
def test_x_square(input):
    n = input
    assert pow(n, 2) == 49


@pytest.mark.skip
def test_s_equality():
    assert 1 == 1
