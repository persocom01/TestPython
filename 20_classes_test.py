import json
import cerberus
import requests

# Write data to file. Push it to github manually.
list1 = [{'name': 'Kuro', 'sex': 'M', 'color': 'Black'},
         {'name': 'Shiro', 'sex': 'F', 'color': 'White'}]
with open('file3.txt', 'w') as f:
    json.dump(list1, f, sort_keys=False, indent=4, ensure_ascii=False)

# Demonstrates use of requests to retrieve file online.
r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/file3.txt')

list2 = json.loads(r.text)

# Demonstrates use of cerberus validator.
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


class Animal:
    def __init__(self, name='', sex='', color=''):
        self.name = name
        self.sex = sex
        self.color = color

# Demonstrates creation of subclass


class Cat(Animal):
    def sound(self):
        print('Meow')


# for i, dic in enumerate(list2):
#     exec 'cat%s=Cat(dic['name'], dic['sex'], dic['color'], )' % i

# Kuro = Cat(**list2[0])
# Kuro.sound()
# print(Kuro.sex)
# print(Kuro.color)
