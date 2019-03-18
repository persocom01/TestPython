import os
import json
import cerberus
import requests
os.chdir(os.getcwd() + r'\files')

# Write data to file. Push it to github manually.
list1 = [{'name': 'Kuro', 'sex': 'M', 'color': 'Black'},
         {'name': 'Shiro', 'sex': 'F', 'color': 'White'}]
with open('file3.txt', 'w') as f:
    json.dump(list1, f, sort_keys=False, indent=4, ensure_ascii=False)

# Demonstrates use of requests to retrieve file online.
r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/files/file3.txt')

# request module contains its own json decoder, so json.load isn't required.
list2 = r.json(r.text)

# Demonstrates use of cerberus validator.
# If only the type needs to be validated, use isinstance(object, type) instead.
schema = {
    'sex': {'type': 'string', 'allowed': ['M', 'F']}
}

# allow_unknown=True allows unknown keys to exist.
v = cerberus.Validator(schema, allow_unknown=True)

for key in list2:
    if not v.validate(key):
        raise Exception('Wrong value for sex.')
        print(v.errors)

# Demonstrates creation of class.
# In this case a dictionary is used to set instance attributes.


class Animal:
    def __init__(self, dictionary):
        self.trick = []
        for k, v in dictionary.items():
            setattr(self, k, v)

    def add_trick(self, trick):
        self.trick.append(trick)

# Demonstrates creation of subclass


class Cat(Animal):
    def sound(self):
        print('Meow')


Kuro = Cat(list2[0])
Kuro.add_trick('claw rush')
Kuro.sound()
print(Kuro.name, Kuro.sex, Kuro.color)
print(Kuro.trick)

# It is also possible for a subclass to inherit from multiple classes.
# In those cases the leftmost superclass takes priority.
