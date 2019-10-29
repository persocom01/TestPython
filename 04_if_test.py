# Demonstrates bsic if statement, as well as how to ask for input.
x = int(input('Please enter an integer: '))

# Technically you can write if statements in 1 line, such as
# if x == 0: do something.
if x == 0:
    print('you entered zero')
# It is possible to use operators like this in python, but not
# in vba.
elif 10 > x > 0:
    print('{} is between 10 and zero'.format(x))
else:
    print(str(x) + ' is smaller than zero')
