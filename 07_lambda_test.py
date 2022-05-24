# Demonstration of various ways to use lambda functions.
from functools import reduce


def signal(x): return 'Buy' if x <= 25 else 'Sell' if x >= 75 else 'No change'


data = [50, 10, 90]
action = list(map(signal, data))
print('function result:', action)
# The lambda function used here is the equivalent of the function above
action = list(map(lambda x: 'Buy' if x <= 25 else 'Sell' if x >= 75 else 'No change', data))
# map functions can alternatively be written as list comprehensions like this:
# action = [signal(x) for x in data]
print('lambda result:', action)

action = list(filter(lambda x: x == 'Buy' or x == 'Sell', action))
# filter functions can alternatively be written as list comprehensions:
# action = [x for x in action if x == 'Buy' or x == 'Sell']
print(action)

# Demonstrates reduce function, which applies a function to the first value,
# retains the result, and repeats for the next value in a list.
trend = reduce(lambda x, y: (x + y)/2, data)
print(trend)
