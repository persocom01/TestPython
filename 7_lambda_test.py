# Demonstration of various ways to use lambda functions.
signal = lambda x: 'Buy' if x <= 25 else 'Sell' if x >= 75 else 'No change'
print(signal(80))

data = [50, 10, 90]
action = list(map(signal, data))
# map functions can alternatively be written as list comprehensions like this:
# action = [signal(x) for x in data]
print(action)

action = list(filter(lambda x: x == 'Buy' or x == 'Sell', action))
# filter functions can alternatively be written as list comprehensions like this:
# action = [x for x in action if x == 'Buy' or x == 'Sell']
print(action)

# Demonstrates reduce function, which applies a function to the first value, retains the result,
# and repeats for the next value in a list.
from functools import reduce
trend = reduce(lambda x, y: (x + y)/2, data)
print(trend)
