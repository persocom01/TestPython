class Animal:
    def __init__(self, color=''):
        self.legs = 4
        self.color = color


class Feline:
    def __init__(self, color=''):
        self.legs = 3
        self.color = color


class Cat(Feline, Animal):
    def sound(self):
        print('Meow')


Kuro = Cat('Black')
print(Kuro.legs)
