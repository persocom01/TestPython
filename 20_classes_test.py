import json
import cerberus
import requests

# Write data to file.
list1 = [['M', 'Black'], ['F', 'White']]
with open('file3.txt', 'w') as f:
    json.dump(list1, f, sort_keys=True, indent=4, ensure_ascii=False)

r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/file3.txt')

list2 = json.loads(r.text)

schema = {
    'sex': {'type': 'string', 'allowed': ['M', 'F']}
}
v = cerberus.Validator(schema)

for key in list2:
    print(v.validate(list2[key]))

# class Animal:
#     def __init__(self, sex='', color=''):
#         self.sex = sex
#         self.color = color
#
# class Cat(Animal):
#     def sound(self):
#         print('Meow')
#
# Kuro = Cat('M', 'Black')
# Kuro.sound()
# print(Kuro.sex)
#
