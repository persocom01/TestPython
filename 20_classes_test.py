import json
import cerberus
import requests

# Write data to file.
dic = {'Kuro': ['M', 'Black'], 'Shiro': ['F', 'White']}
with open('file3.txt', 'w') as f:
    json.dump(dic, f, sort_keys=True, indent=4, ensure_ascii=False)

r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/file3.txt')

print(r)
#
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
# schema = {
#     'sex': {'type': 'string', 'allowed': ['M', 'F']}
#     }
# v = cerberus.Validator(schema)
# print(v.validate(Kuro.sex))
