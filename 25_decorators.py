# Demonstrates use of decorators in python.
# Decorators are functions that modify and return other functions.


def amplify(old_function):
    def new_function(x):
        return old_function(x*10)
    return new_function


def addon(old_function):
    def new_function(x):
        return old_function(x+10)
    return new_function


# @ is used above the function to modified.
@amplify
def times2(x):
    return x*2


# You may even use multiple decorators.
# In such case the higher decorators go first.
# In this case, ((1 + 10) * 10) + 1 = 111
@addon
@amplify
def plus1(x):
    return x+1


print(times2(1))
print(plus1(1))
