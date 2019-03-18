# Demonstrates a simple function calling another
def interface():
    print('Welcome')
    # Demonstrates two ways to give functions argument values. First by
    # position order, second by using the keyword.
    passwordfunc('a', tryagain='Opps')

# Demonstrates use of default values.


def passwordfunc(password, retries=1, tryagain='Please try again',
                 fail='No more tries left'):
    while retries > 0:
        userinput = input('Please enter the password')
        if userinput == password:
            print('Correct!')
            break
        else:
            retries -= 1
            if retries > 0:
                print(tryagain)
            else:
                print(fail)


interface()

# Demonstrates how using mutable objects as arguments can be used to build
# a function with a mutable result.


def mutablefunc(a, L=[]):
    L.append(a)
    return L


print(mutablefunc(1))
print(mutablefunc(2))
