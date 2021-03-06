# Demonstrates error handling.
file = './files/file2.txt'

# Demonstrates handling of multiple errors in a line using a tuple.
# It may also be preferrable to write the tuple directly into the except
# statement without defining a variable.
errors = (FileNotFoundError, NameError)
try:
    f = open(file, 'r')
    r = f.readline()
    i = int(r.strip())
# Change to non existant file or variable name to get this error.
except errors as err:
    print('File or variable error: {0}'.format(err))
except ValueError as err:
    print('Value error: {0}'.format(err))
# Catches all other exceptions. Using except: does the same thing,
# but in this case we want to print the error.
# The order matters. Since this catches all exceptions, putting it above the
# other errors will cause them to never trigger.
except Exception as err:
    print('Other errors: {0}'.format(err))
# else is executed when no exceptions are encountered.
# It must come after except statements.
else:
    f.close()
# finally is executed no matter what.
finally:
    print()

# --------------------------------------------------------------------------------
# Demonstrates the creation and raising of custom errors.


class MyError(Exception):
    def __init__(self, value, message='User defined error encountered from value:'):
        self.value = value
        self.message = message
        Exception.__init__(self, '{0} {1}'.format(message, value))


class OverValError(MyError):
    def __init__(self, value, message='The input value is over 10:'):
        self.value = value
        self.message = message
        Exception.__init__(self, '{0} {1}'.format(message, value))


var = 20
# Customized error msg to occur.
underval_error = Exception('Value is under zero.')
try:
    if var < 0:
        # Demonstrates use of raise to force an error or in this case,
        # customized error msg to occur.
        raise underval_error
    elif var > 10:
        # One can replace this custom error with any of the python built-in
        # error types. The standard ones are found here:
        # https://www.tutorialspoint.com/python/standard_exceptions.htm
        raise OverValError(var)
except OverValError:
    # Demonstrates use of raise to re-raise the error.
    raise
    # pass

# Demonstrates use of assert to raise errors. assert is roughly equal to:
# if not assert_condition:
#     raise AssertionError()
assert 1 == 1
