# Demonstrates bsic if statement, as well as how to ask for input.
x = int(input('Please enter an integer: '))

if x == 0:
    print('you entered zero')
elif x > 0:
    print('{} is greater than zero'.format(x))
else:
    print(str(x) + ' is smaller than zero')
