# Demonstrates use of decorators in python.
# Decorators are functions that modify and return other functions.


def amplify_input(old_function):
    def decorated(x):
        return old_function(x*10)
    return decorated

# Demonstrates how to pass arguments to decorators.


def add_to_input(y):
    def add(old_function):
        def decorated(x):
            return old_function(x + y)
        return decorated
    return add


# @ is used above the function to modified.
@amplify_input
def times2(x):
    return x*2


# You may even use multiple decorators.
# In such cases the higher decorators go first.
# In this case, ((1 + 10) * 10) + 1 = 111
@add_to_input(10)
@amplify_input
def plus1(x):
    return x+1


print(times2(1))
print(plus1(1))
