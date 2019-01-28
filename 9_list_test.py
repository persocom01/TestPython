# Demonstrates various function methods.
from collections import deque
from functools import reduce

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

print(fruits.count('apple'))
print(fruits.index('apple'))
# Find an instance of apple starting at index 2.
print(fruits.index('apple', 2))

# Demonstrates copy and reverse functions.
# The significance of copy() is that the value remains unchanged when the
# original variable is modified.
fruits2 = fruits.copy()
fruits2.reverse()
print('Reverse:', fruits2)

fruits.append('grape')
fruits.extend(['mango', 'papaya'])
print('Append:', fruits)

# Of note is the face remove only removes the first matching element.
fruits.remove('apple')
print('Remove:', fruits)

fruits.sort()
print('Sort:', fruits)

# Removes last entry and returns it. Can be used with append to make a stack.
print(fruits.pop())
print('pop:', fruits)

# Delates list.
print(fruits.clear(), '\n')

# Imports a type of list where append and pop functions can be applied to the
# beginning.
enemies = deque(['Orc', 'Goblin', 'Catapult'])

enemies.appendleft('Slime')
print('append:', enemies)
print('You struck down the ' + enemies.popleft() + '.')
print('You struck down the ' + enemies.popleft() + '.')
print('Enemies left:', enemies)

# Demonstrates 2d list.

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Demonstrates looping through 2d list using a nested loop.
for row in grid:
    print(row)
    for element in row:
        avg = reduce(lambda x, y: (x + y)/2, row)
    print(avg)
