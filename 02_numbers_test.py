# Demonstrates common functions used with numbers.
import math
import random
import statistics
import decimal

# Absolute value.
print(abs(-123))
print()

# Powers.
x = 5**2
print(x)
print(pow(5, 2))
print(math.sqrt(25))
print()

# Larger/smaller number.
print(max(5, 2))
print(min(5, 2))
print()

# Rounding.
print(round(1.5))
print(math.floor(1.7))
print(math.ceil(1.2))
print()

# Compound assingment operators.
y = 1
y += 1
y -= 1
y *= 10
y /= 2
print('start:', y)
# Use this if you want the result to be an integer.
y //= 2
print('divide and floor:', y)
y **= 2
print('power:', y)
y %= 2
print('remainder:', y)
print()

# Different randomizations.
print(random.choice(['one', 'two', 'three']))
# No repeats.
print(random.sample(range(100), 10))
# Set random seed.
random.seed(123)
# Similar to excel's rand()
print(random.random())
# Rand int from 1-10.
print(random.randrange(1, 11))
print()

# Stat functions.
data = [75, 25, 250, 50]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
print()

# Demonstrates use of the decimal module for calcuations involving fractions
# that give weird results in floating point. Alternatively, multiply all input
# by a factor of 10.
print(1.00 % 0.10)
print(decimal.Decimal('1.00') % decimal.Decimal('.10'))
print()

# Alternatively, use math.isclose() to prevent floating point precision errors.
print(0.1 + 0.7 == 0.8)
print(math.isclose(0.1 + 0.7, 0.8))
