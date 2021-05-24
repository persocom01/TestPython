# Deonstrates basic pytest functions, as well as the grouping by test name.
import math


# To test this function only, use the command:
# pytest -k math
def test_math_sqrt():
    n = 25
    assert math.sqrt(n) == 5


# pytest -k others
def test_others_square():
    n = 8
    assert pow(n, 2) == 49


def test_others_equality():
    assert 1 == 1
