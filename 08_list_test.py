# Demonstrates various list methods.
from collections import deque
from functools import reduce
import bisect

# List names are plural by convention.
# Lists are considered mutable objects, thus when var = list is used, the list
# is passed by reference instead of by value. As a result, any changes to list
# will affect var.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

# Size of list.
print(len(fruits))
print(fruits.count('apple'))
# If you just need to know if a value is in a list, use: value in list.
print(fruits.index('apple'))
# Find an instance of apple starting at index 2.
print(fruits.index('apple', 2))
# slice() works on lists as it does strings.
print('slice:', fruits[slice(0, 10, 2)])

# Demonstrates copy and reverse functions.
# The significance of copy() is that the value remains unchanged when the
# original variable is modified.
fruits2 = fruits.copy()
# It is also possible to reverse the list without altering the original using
# list(reversed(fruits))
fruits2.reverse()
print('reverse:', fruits2)

fruits.append('grape')
# extend is like append, but for lists. It returns None. If you wish to return
# the combined lists instead, use result = list1 + list2
fruits.extend(['mango', 'papaya'])
print('append:', fruits)

# Of note is the face remove only removes the first matching element.
fruits.remove('apple')
print('remove:', fruits)

fruits.sort()
print('sort:', fruits)

# Demonstrates sorting using a function as key.
# Alternatively, use key=lambda x: x[-1].


def last_letter(x):
    return x[-1]


fruits.sort(key=last_letter)
print('sort by last letter:', fruits)

# list.pop(index=None) removes last entry and returns it.
# If index is given it removes the correspending list element.
# Can be used with append to make a stack.
print(fruits.pop(2))
print('pop:', fruits)

# Demonstrates use of bisect module to replace a deleted key from a list.
fruits_numbered = list(enumerate(fruits))
key = 2
del fruits_numbered[key]
bisect.insort(fruits_numbered, (key, 'guava'))
print(fruits_numbered)

# Deletes list.
fruits.clear()
print()

# Imports a type of list where append and pop functions can be applied to the
# beginning.
enemies = deque(['Orc', 'Goblin', 'Catapult'])

enemies.appendleft('Slime')
print('append:', enemies)
print('You struck down the ' + enemies.popleft() + '.')
print('You struck down the ' + enemies.popleft() + '.')
print('Enemies left:', enemies)
print()

# Demonstrates mathematical operations between number lists
nums = [1, 2, 3]
nums2 = [3, 2, 1]
result = []
for e, e2 in zip(nums, nums2):
    result.append(e - e2)
print('subtraction between lists:')
print(result)
print()

# Demonstrates 2d list.
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Note how indexing works on a 2d list.
print(grid[2])
# Demonstrates looping through 2d list using a nested loop.
for row in grid:
    print(row)
    print('Sum:', sum(row))
    for element in row:
        mavg = reduce(lambda x, y: (x + y)/2, row)
    print('Mavg:', mavg)
print()
