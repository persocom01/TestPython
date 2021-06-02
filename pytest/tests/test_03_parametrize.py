# Demonstrates using a multiple inputs with a single test function.
import math
import pytest


# Note how it is possible to combine groupings with parametrize.
@pytest.mark.math
@pytest.mark.parametrize('i, o', [(25, 30), (9, 3)])
def test_param_sqrt(input, i, o):
    n = i
    assert math.sqrt(n) + input == o


@pytest.mark.others
@pytest.mark.parametrize('i, o', [(25, 49), (7, 49)])
def test_param_square(i, o):
    n = i
    assert pow(n, 2) == o
