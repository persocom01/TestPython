# pytest

A pytest testing playground organized by topic in the pytest tutorial: https://www.tutorialspoint.com/pytest/index.htm

## Installation

The pytest module needs to be installed:

```
pip install pytest
```

## Usage

pytest runs python files starting with `test_` in the root folder and `test` subfolder. An error is returned if any of the files share the same name. When the files are run, pytest executes every function in the file whose name starts with `test_`. Unlike file names, functions can share the same name so long as they are in different files. To run pytest, enter the following into command line in the root folder:

```
pytest optional_filename
```

`-v` = makes the result more detailed, notable it lists which test files succeeded.
`-k test_string` = runs only the test functions which contain test_string in their names.
`-m test_marker` = runs only test functions with test_marker in their marker name. If the markers are not defined in `pytest.ini`, an error message will be returned, but the test will still run. Alternatively `-m "not test_marker"` can be used to test everything except the tests with the marker name.
`--strict-markers` = Tests with markers not defined in `pytest.ini` will not be run and an error is returned instead.
`-ra = -r` for summary and -a for all except passes. These tags are often used to shorten the error report.
`--maxfail = number` = the maximum number of failures for the test to be considered failed.

Giving a filename results in that file being the only one tested.

### markers

markers is how tests are grouped in pytest. A marker is defined for a function in the following way:

```
@pytest.mark.mark_name
def test_name():
  asset 1 == 1
```

### Special markers

pytest has the following special markers that need no definition in `pytest.ini`:

1. parametrize

parametrize is a special marker in pytest that allows one to define multiple arguments in a test. It cannot be mixed with other markers, nor can fixture be defined as one of the inputs in the mark. However, fixture can be defined as an input of the function itself. For example:

```
@pytest.mark.parametrize("i, o", [(25, 30), (9, 3)])
def test_param_sqrt(fixture_input, i, o):
    n = i
    assert math.sqrt(n) + fixture_input == o
```

parametrize arguments are defined in the form `("arg1, arg2", [(arg1_value1, arg2_value1), (arg1_value2, arg2_value2)])`.

2. xfail

xfail causes a test to be run, but no details to be printed regardless of whether it passes or fails. It will only be in the summary results, for example:

```
======================= 6 failed, 6 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 warning in 0.33s =======================
```

3. skip

A skip marker causes the test not to be run at all. It will only be recorded in the result summary as "skipped".

### fixture

fixture is how you define inputs in pytest. For example:

```
@pytest.fixture
def input():
   i = 1
   return i

def test_assert_input(input):
  assert input == 1
```

In this case, the fixture function is used to define the input value for all tests in the same file that accept it as an argument. For simple input values, one can define a global variable in the same file instead. However, if the fixture is put into the `conftest.py` in the root directory, it would apply to all test files, something which a global variable cannot do.

## Configuration

pytest can be optionally configured in the following files:
* `pytest.ini`
* `pyproject.toml`
New in 6.0.
* `tox.ini`

They can be located in the root folder or `test` subfolder. If more than one exists, the file higher in this list will take priority and the rest are ignored.

### pytest.ini or tox.ini

Configuration of `pytest.ini` is as follows:

```
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    .
    tests
    integration
markers =
    math: marks tests of the math module (deselect with '-m "not math"')
    others
```

`.` under testpaths tells pytest to search the root folder for test files.

Alternatively, the configuration options in `pytest.ini` can be written in `tox.ini` instead.

### pyproject.toml

Configuration of `pyproject.toml` is similar to `pytest.ini`

```
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    ".",
    "tests",
    "integration",
]
markers = [
    "math: marks tests of the math module (deselect with '-m \"not math\"')",
    "others"
]
```
