# Demonstrates various function methods.
from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

print(fruits.count('apple'))
print(fruits.index('apple'))
# Find an instance of apple starting at index 2.
print(fruits.index('apple', 2))

fruits.reverse()
print('Reverse:', fruits)

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
