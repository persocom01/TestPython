# Demonstrates creation of tuples.
tuple = ()
print(tuple)
tuple = ('first',)
print(tuple)
tuple = 'first', 'second', 'third'
print(tuple)

# Demonstrates the use of sets, which have no duplicates.
fruits1 = ['apple', 'apple', 'banana', ]
fruits1 = set(fruits1)
print(fruits1)

# Demonstrates different set operations.
fruits2 = set(['apple', 'orange', ])
print('Minus:', fruits1 - fruits2)
print('Merge:', fruits1 | fruits2)
print('And:', fruits1 & fruits2)
print('Unique:', fruits1 ^ fruits2)

# Demostrates use of dictionary.
items = {'Weapon': 'Bow', 'Armor': 'Leather armor', }
# Alternatively:
# items = dict([('Weapon', 'Bow'), ('Armor', 'Leather armor')])
# items = dict(Weapon='Bow', Armor='Leather armor')
items['Ammo'] = 'Arrows'
print(items['Ammo'])

# It is not possible to directly sort a dictionary.
# However, a new list can be generated with sorted values and a new dictionary
# can be written (or the old one overwritten) using the sorted keys.
sorted_keys = sorted(items)
sorted_items = {x: items[x] for x in sorted_keys}
print('Sort by keys:', sorted_items)

# It is also possible to sort in other ways using this method.
sorted_values = sorted(items.values())
print('Sort by values:', sorted_values)

# Another key of note is key=str.lower to ignore case while sorting.
# Also possible to use another list as key.
sort_by_values_but_return_keys = sorted(
    items, key=items.__getitem__, reverse=False)
print('Sort by values but return keys:', sort_by_values_but_return_keys)

# Note the reverse argument which reverses the order of the result.
sort_by_function = sorted(
    items, key=(lambda x: 0 if 'a' in x else 1), reverse=True)
print(sort_by_function)
