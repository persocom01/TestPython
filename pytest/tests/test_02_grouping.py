# Deonstrates groupings and fixtures in pytest.
import math
import pytest

# To test this function only, use the command:
# pytest -m math
@pytest.mark.math
def test_sqrt(input):
    n = input
    assert math.sqrt(n) == 5


# pytest -m others
@pytest.mark.others
def test_square(input):
    n = input
    assert pow(n, 2) == 49


@pytest.mark.others
def test_equality():
    assert 1 == 1
