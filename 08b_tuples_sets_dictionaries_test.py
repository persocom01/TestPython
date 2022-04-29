# Demonstrates creation of tuples.
tuple = ()
print(tuple)
tuple = ('first',)
print(tuple)
tuple = 'first', 'second', 'third'
print(tuple)
print()

# Demonstrates the use of sets, which have no duplicates.
print('unique elements: ', len({'apple', 'apple', 'banana', }))
fruits = ['apple', 'apple', 'banana', ]
# Sets are defined by {}. However since {} also define dictionaries, sets are
# typically created using set() instead. In cases when set(str) is used, the
# string will be considered a list of numbers. To pass the whole string, use
# set([str]) instead.
fruits = set(fruits)
print(fruits)
# Sets cannot be sorted, but you can use sorted to return a sorted list.
print('Sorted:', sorted(fruits))

# Demonstrates different set operations.
fruits2 = set(['apple', 'orange', ])
print('minus:', fruits - fruits2)
print('merge:', fruits | fruits2)
# symmetric_difference is the opposite of a merge, and is equivalent to
# (setA - setB) + (setB - setA)
print('symmetric_difference:', fruits.symmetric_difference(fruits2))
print('and:', fruits & fruits2)
print('unique:', fruits ^ fruits2)
fruits2.add('peach')
print('add:', fruits2)
# Use update to add multiple elements to a set.
fruits2.update(['papaya'])
print('update:', fruits2)
fruits2.remove('papaya')
print('remove:', fruits2)
print()


# Dictionaries are normally accessed through dict[key]. However, in some cases,
# dict.key might be preferable. This class allows dictionary-like objects to be
# instantiated using either
# Adict = AttribDict(dict)
# Adict = AttribDict(param1=value1, param2=value2)
# and accessed using attributes instead of []. They are, however, not actual
# dictionaries and some dictionary methods may fail.
class AttribDict(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])


# Demonstrates use of dictionary.
# Alternatively:
# items = dict([('Weapon', 'Bow'), ('Armor', 'Leather armor')])
# items = dict(Weapon='Bow', Armor='Leather armor')
items = {'Weapon': 'Bow', 'Armor': 'Leather armor', }
items2 = {'Helmet': 'Steel helmet'}

# Demonstrates attribute dictionaries.
Aitems = AttribDict(items)
print('attribute dictionary: ' + Aitems.Weapon)
# Demonstrates adding key to dictionary.
items['Ammo'] = ['Wood arrows']
# Demonstrates appending to a key containing a list.
items['Ammo'].append('Iron arrows')
# Demonstrates adding dictionaries together.
# In cases where this doesn't work, use:
# items = dict(list(items.items()) + list(items2.items()))
# Note that the above causes items in list2 to overwrite items in list1.
items.update(items2)
print('adding dictionaries together:', items)
# Demonstrates get function. A default value can be specified in case
# the key does not exist. In this case the default is 'No ammo.'
# If the value of a key is another dictionary, get can be chained to get values
# from deeper keys.
print('get:', items.get('Ammo', 'No ammo.'))
# Demonstrates deleting a key from a dictionary.
# It is possible to use del items['Ammo'] instead, but it will return an error
# if the key is not found.
items.pop('Ammo', None)
print()

# Demonstrates getting multiple keys from a dictionary.
# Alternatively:
# import operator as op
# op.itemgetter('Weapon', 'Armor')(items)
# This method returns the items only, and not a modified dictionary.
keys = ['weapon', 'armor']
multiple_keys = {k: v for k, v in items.items() if k.lower() in keys}
print('multiple_keys:', multiple_keys)

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
    # This function sorts words with 'r' in them towards the back then reverses
    # the order.
    items, key=(lambda x: 1 if 'r' in x else -1), reverse=False)
print('Sort by function:', sort_by_function)

# items() is a useful function on dictionaries to turn key: value
# into tuples.
print(items.items())
