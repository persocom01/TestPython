import cerberus

class Animal:
    def __init__(self, sex='', color=''):
        self.sex = sex
        self.color = color

class Cat(Animal):
    def sound(self):
        print('Meow')

Kuro = Cat('M', 'Black')
Kuro.sound()
print(Kuro.sex)

schema = {
    'sex': {'type': 'string', 'allowed': ['M', 'F']}
    }
v = cerberus.Validator(schema)
print(v.validate(Kuro.sex))
