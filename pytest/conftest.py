import pytest

# fixture is used to define inputs for test functions in the same file in
# pytest. It is possible to define a global variable instead. However, fixtures
# can do much more complicated things such as retreive data from the database.
@pytest.fixture
def input():
    i = 25
    return i
